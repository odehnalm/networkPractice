from threading import Thread
import socket
import display
import netutils
from netutils import read_line
import random

def main(): # called at the end of the file
    d = display.Display()
    # start a new thread to accept new connections
    handle_acceptall(d).start()


def handle_acceptall(d):
    def handle():
        # create a socket that listens (on a port of your choice)

        server_socket = socket.socket()
        port = 9999
        server_socket.bind(('', port))
        print("socket binded to %s" % port)
        server_socket.listen()
        print("socket is listening")
        # accept new clients connections,
        # and start a handle_client thread every time


        # a forever loop until we interrupt it or
        # an error occurs
        while True:
            # Establish connection with client.
            socket_c, addr = server_socket.accept()
            print ('Got connection from', addr)
            handle_client(socket_c,d).start()

    t = Thread(target=handle)
    return t


# handle_client returns a Thread that can be started, i.e., use: handle_client(.......).start()
def handle_client(socket,d):
    def handle():
        # initialise a random integer position, e.g. between 0 and 100
        i = random.randint(0, 100)
        print(i)
        # initialize a random direction (for later)
        by = random.choice([-1, 1])

        # add 1 to the display, at index i (and render it)
        d.add_value(i, 1)
        d.render()


        # loop over the received data, ignoring (or just printing) this data for now (e.g., use netutils to read lines)
        # be sure to end the loop when the connection is closed (readLine returns None or throws an exception)
        while True:
            # read two lines then ignore anything from this client...
            l = netutils.read_line(socket)
            print("RECEIVED Message:", l)

            # Magic word is sent
            magic_word = 'sharmuta'
            print(l == magic_word)
            if l == magic_word:
                d.move_value_right(i,by,1)
                i = i + 1*by
                d.render()

            if l is None:
                break
            # ... ignore the rest

        # Later, we will use move_value_right(i, by) and increase the i variable by
            # DONE

        # when the connection is closed, subtract at index (and rerender)
        d.add_value(i, -1)
        d.render_clean()

    t = Thread(target=handle)
    return t


if __name__== "__main__":
  main()
