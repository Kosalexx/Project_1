import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen()

while True:
    print("Server is ready to accept connection.")
    client_socket, addr = server_socket.accept()
    message = bytes()
    BUFF_SIZE = 8
    while True:
        data = client_socket.recv(BUFF_SIZE)
        message += data
        if len(data) < BUFF_SIZE:
            break
    client_socket.sendall(message)
