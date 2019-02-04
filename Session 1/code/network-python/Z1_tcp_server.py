import socket
import netutils

server_socket = socket.socket()
server_socket.bind(('localhost', 9999))
server_socket.listen()
print(server_socket)

# process clients one by one (not in parallel)
while True:
    print("Waiting for connection")
    socket, addr = server_socket.accept()
    print("Received connection", socket)
    # read two lines then ignore anything from this client...
    l = netutils.read_line(socket)
    print("RECEIVED FIRST:", l)
    l = netutils.read_line(socket)
    print("RECEIVED SECOND:", l)
    # ... ignore the rest
