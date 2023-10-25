import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.bind(('', 8080))
    sock.listen(1)
    connection, address = sock.accept()
    request = connection.recv(1024)
    while True:
        if input() == 'quit':
            break
    connection.close()

if __name__ == '__main__':
    main()
