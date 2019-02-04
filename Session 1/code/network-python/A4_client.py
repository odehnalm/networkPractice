import socket
import time
import random

def main(): # called at the end of the file
    # pass # TODO, taking inspiration of the rest

    TCP_IP = '127.0.0.1'
    TCP_PORT = 9999
    magic_word = b'sharmuta\r\n'
    # BUFFER_SIZE = 20

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((TCP_IP, TCP_PORT))

        for i in range(50):
            time.sleep(random.random()/10)
            s.sendall(magic_word)

        s.close()

if __name__== "__main__":
  main()
