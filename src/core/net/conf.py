from socket import *
import pickle

HOST = gethostbyname(gethostname())
PORT = 5000
ADDR = (HOST, PORT)

MAX_PLAYERS = 5
MSGLEN = 1024

__all__ = [

    # socket API
    "socket",
    "AF_INET", "SOCK_STREAM", "SHUT_RDWR",

    # pickle API
    "pickle",

    # global server conf
    "ADDR", "MAX_PLAYERS", "MSGLEN"
]
