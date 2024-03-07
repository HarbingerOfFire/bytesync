import argparse, time

class args:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser("bytesync")
        self.init_args()

    def init_args(self):
        self.parser.add_argument("-o", "--outfile", action="store", default=f"bytesync_{time.time_ns()}.txt")
        self.parser.add_argument("-l", "--listen", action="store_true")
        self.parser.add_argument("-t", "--transmit", action="store_true")
        self.parser.add_argument("-p", "--port", action="store", default="20")
        self.parser.add_argument("-H", "--host", action="store", default="localhost")
        self.parser.add_argument("-f", "--file", action="store")
    
    def return_args(self):
        return self.parser.parse_args()
