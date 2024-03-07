import socket
class listen:
    def __init__(self, HOST, PORT:int) -> None:
        self.HOST=HOST
        self.PORT=PORT

    def listen(self, outfile):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.HOST, self.PORT))
            s.listen(1)
            conn, addr = s.accept()
            with conn:
                try:
                    file=open(outfile, "wb")
                except: pass
                while True:
                    data=conn.recv(1024)
                    if not data:
                        break
                    if outfile:
                            file.write(data)
                    else:
                        print(data.decode())