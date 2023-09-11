import socket


BUFF_SIZE = 8


def send_message(message: str, buff_size: int) -> str:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 5000))
    bytes_message = message.encode('UTF-8')
    client_socket.sendall(bytes_message)
    returned_message = bytes()
    while True:
        data = client_socket.recv(buff_size)
        returned_message += data
        if len(data) < buff_size:
            break
    string_result = returned_message.decode('UTF-8')
    client_socket.close()
    return string_result


text = input('Enter your text: ')
result = send_message(text, BUFF_SIZE)
print(f'The most common word: "{result}".')
