import select
import socket

ECHO_PORT = 9999
BUF_SIZE = 4096


def main():
    print("----- Echo Server -----")
    try:
        server_socket = socket.socket()
    except socket.error as err:
        print("socket creation failed with error %s" % (err))
        exit(1)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('127.0.0.1', ECHO_PORT))
    server_socket.listen(5)

    fd_map = {server_socket.fileno(): server_socket}

    poller = select.poll()
    poller.register(server_socket, select.POLLIN)

    while True:
        events = poller.poll()
        for fd, event in events:
            if fd == server_socket.fileno():
                client, addr = server_socket.accept()
                print("Connection from ", addr)
                poller.register(client, select.POLLIN | select.POLLERR)
                fd_map[client.fileno()] = client

            elif event & select.POLLIN:
                data = fd_map[fd].recv(1024)
                fd_map[fd].send(data)


if __name__ == '__main__':
    main()
