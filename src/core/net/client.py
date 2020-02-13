from .conf import *


class Client:
    _player = None

    def __init__(self, player, _socket=None):
        self._player = player
        if _socket is None:
            self.socket = socket(AF_INET, SOCK_STREAM)
        else:
            self.socket = _socket

    def connect(self):
        self.socket.connect(ADDR)

    def disconnect(self):
        # self.socket.shutdown(SHUT_RDWR)
        self.socket.close()

    def receive(self):
        chunks = []
        chunk = self.socket.recv(1024)
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        print(chunk.decode("utf-8"))
        return b''.join(chunks)

    def send(self):
        data = pickle.dumps(self._player)
        try:
            self.socket.sendall(data)
            r = self.receive()
            print(r.decode("utf-8"))
        except Exception as e:
            print(e)
