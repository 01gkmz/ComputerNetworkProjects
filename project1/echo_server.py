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
    server_socket.setblocking(False)

    epoller = select.epoll()
    epoller.register(server_socket.fileno(), select.EPOLLIN|select.EPOLLET)

    connections = {}
    addresses = {}
    
    while True:
        events = epoller.poll()
        for fd, event in events:
            if fd == server_socket.fileno():
                client, addr = server_socket.accept()
                print("Connection from ", addr)

                connections[client.fileno()] = client
                addresses[client.fileno()] = addr

                epoll.register(client.fileno(), select.EPOLLIN|select.EPOLLET)

            elif event == select.EPOLLIN:
                data = connections[fd].recv(1024)

                if data:
                    connections[fd].send(data)
                else:
                    connections[fd].close()


if __name__ == '__main__':
    main()
