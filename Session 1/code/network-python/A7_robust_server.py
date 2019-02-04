from threading import Thread
import socket
import display
import netutils
import random
import queue

# Main function
def main(): # called at the end of the file

    # Prepares the queue of tasks to be performed by the consumer
    q = queue.Queue()

    # Initiate the consumer program who deals with printings
    c = consumer(q)
    c.daemon = True # NB: the program terminates when all non-daemon thread are done
    c.start()

    # Start to receive request from clients
    handle_acceptall(q).start()

# This is the server, opens the socket in order to receive requests
def handle_acceptall(q):
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
            # The producer will handle connections with clients
            producer(socket_c,q).start()

    t = Thread(target=handle)
    return t


# handle_client returns a Thread that can be started, i.e., use: handle_client(.......).start()
def producer(socket,q):
    def handle():

        # NOTE: we will put in queue a tuple where the components:
        # 0: position
        # 1: amount to sum
        # 2: move left or right
        # 3: action to perform (LOGIN, MAGIC, LOGOUT)

        # initialise a random integer position, e.g. between 0 and 100
        i = random.randint(0, 100)
        # print(i)
        # initialize a random direction (for later)
        by = random.choice([-1, 1])

        # add 1 to the display, at index i (and render it)
        # LOGIN
        q.put((i, 1, by,'LOGIN'))

        # WE TELL CONSUMER THAT I HAVE NEW CONNECTION AND DISPLAY IT

        # loop over the received data, ignoring (or just printing) this data for now (e.g., use netutils to read lines)
        # be sure to end the loop when the connection is closed (readLine returns None or throws an exception)
        while True:
            # read two lines then ignore anything from this client...

            # $$$ PUT STUFF ON QUEUE IF I HAVE THE MAGIC WORD
            l = netutils.read_line(socket)
            print("RECEIVED Message:", l)

            # MAGIC word is sent
            magic_word = 'sharmuta'
            if l == magic_word:
                q.put((i, 1,by,'MAGIC'))
                i = i + 1*by

            if l is None:
                break
            # ... ignore the rest

        # Later, we will use move_value_right(i, by) and increase the i variable by
            # DONE

        # when the connection is closed, subtract at index (and rerender)
        # LOGOUT
        q.put((i, -1, by, 'LOGOUT'))

    t = Thread(target=handle)
    return t


def consumer(q):

    # The display is only handled by the consumer
    d = display.Display()

    # This calls the function that initializes the server before starting the infinite loop
    handle_acceptall(q)

    def consume():
        while True:
            e = q.get()
            if e[3] == 'MAGIC':
                by = e[2]
                d.move_value_right(e[0], by, 1)
                d.render()
            elif e[3] == 'LOGIN':
                d.add_value(e[0], 1)
                d.render()
            elif e[3] == 'LOGOUT':
                d.add_value(e[0], -1)
                d.render_clean()

    t = Thread(target=consume)
    return t


if __name__== "__main__":
  main()
