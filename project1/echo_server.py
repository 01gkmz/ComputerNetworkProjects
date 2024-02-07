import select
import socket

ECHO_PORT = 9999


def main():
    print("----- Echo Server -----")

    try:
        # Create the server socket
        server_socket = socket.socket()
    except socket.error as err:
        print("socket creation failed with error %s" % (err))
        exit(1)

    # Permits the bind() in line 11 even if another program was recently listening on the same port.
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the server socket to ip address and port
    server_socket.bind(('127.0.0.1', ECHO_PORT))

    # Tell the server socket to start accepting incoming connections from the clients
    server_socket.listen(5)

    # Use non-blocking mode
    server_socket.setblocking(False)

    # Create an epoll object
    epoller = select.epoll()

    # Register interest in read events on the server socket. A read event will occur any time the server socket accepts a socket connection.
    epoller.register(server_socket.fileno(), select.EPOLLIN | select.EPOLLET)

    connections = {}

    while True:

        # Query the epoll object to find out if any events of interest may have occurred.
        events = epoller.poll()

        for fd, event in events:

            if fd == server_socket.fileno():
                # Events are returned as a sequence of (fileno, event code) tuples. fileno is a synonym for file descriptor and is always an integer.
                client, addr = server_socket.accept()
                print("Connection from ", addr)

                # Add to the dictionary
                connections[client.fileno()] = client

                # Register interest in read (EPOLLIN) events for the new socket.
                epoller.register(client.fileno(), select.EPOLLIN | select.EPOLLET)

            else:
                # Get the data from the client
                data = connections[fd].recv(100000)

                # Send the data to the same client
                connections[fd].send(data)


if __name__ == '__main__':
    main()
