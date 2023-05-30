import socketserver


SERVER_HOST = ('127.0.0.1', 5010)


class MyRequestHandler(socketserver.BaseRequestHandler):
    BUFF_SIZE: int = 8

    def handle(self) -> None:
        print(f"Received connection from {self.client_address}")
        message = bytes()
        while True:
            data = self.request.recv(self.BUFF_SIZE)
            message += data
            if len(data) < self.BUFF_SIZE:
                break
        self.request.sendall(message)


if __name__ == '__main__':
    socketserver.TCPServer(
        server_address=SERVER_HOST,
        RequestHandlerClass=MyRequestHandler,
        bind_and_activate=True).serve_forever()
