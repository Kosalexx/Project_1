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
    string_message = message.decode('UTF-8')
    list_message = string_message.replace(",", "").replace(
        ".", "").replace("?", "").replace("!", "").lower().split()
    words_tuple = [(
        word, list_message.count(word)) for word in set(list_message)]
    result = max(words_tuple, key=lambda x: x[1])[0]
    bytes_result = result.encode('UTF-8')
    client_socket.sendall(bytes_result)
    client_socket.close()
