import socket

class transmit:
    def __init__(self, HOST, PORT:int) -> None:
        self.HOST=HOST
        self.PORT=PORT

    def transmit(self, filename):
        infile=open(filename, "rb")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.HOST, self.PORT))
            for message in infile:
                s.sendall(message.strip(b"\n"))