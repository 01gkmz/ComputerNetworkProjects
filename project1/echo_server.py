import select
import socket

ECHO_PORT = 9999
BUF_SIZE = 4096


def main():
    print("----- Echo Server -----")
    try:
        serverSock = socket.socket()
    except socket.error as err:
        print("socket creation failed with error %s" % (err))
        exit(1)
    serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSock.bind(('192.168.16.1', ECHO_PORT))
    serverSock.listen(5)

    fd_map = {serverSock.fileno(): serverSock}

    pollerObject = select.poll()
    pollerObject.register(serverSock, select.POLLIN)

    while True:
        events = pollerObject.poll()
        for fd, event in events:
            if fd == serverSock.fileno():
                client, addr = serverSock.accept()
                print("Connection from ", addr)
                pollerObject.register(client, select.POLLIN | select.POLLERR)
                fd_map[client.fileno()] = client

            elif event & select.POLLIN:
                data = fd_map[fd].recv(1024).decode()
                if not data:
                    pollerObject.unregister(fd)
                    fd_map[fd].close()
                    del fd_map[fd]
                    continue
                print("client: ", data)
                fd_map[fd].send(data.encode())


if __name__ == '__main__':
    main()
