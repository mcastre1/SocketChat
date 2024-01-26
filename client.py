import socket
import threading
import pickle
from Message import Message
from PyQt5.QtCore import pyqtSignal, QObject

HEADER = 64
# Which port should the server use, 5050 just because. Use something is not being used for something else.
PORT = 65432
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Address of server, for now its the local ip address of machine we are running the server in
SERVER = "192.168.86.95"
ADDR = (SERVER, PORT)


class Client(QObject):
    upate_text = pyqtSignal(Message)

    def __init__(self):
        super().__init__()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Socket connects requires a tuple of server address, port.
        self.client.connect(ADDR)

        self.connected = True
        # This is so I can talk to the server without having to close and open multiple times.
        # name = input("Name: ")

        # self.receive()

    def run(self):
        receiving = threading.Thread(target=self.receive)
        receiving.start()

    # We receive and print all messages from server here.
    def receive(self):
        while self.connected:
            msg_length = self.client.recv(HEADER).decode(FORMAT)

            if msg_length:
                msg_length = int(msg_length)
                msg = self.client.recv(msg_length)

                msg = pickle.loads(msg)

                self.upate_text.emit(msg)

    def send(self, msg, sender):
        msg_object = Message(msg, sender, "")
        msg_pickle = pickle.dumps(msg_object)
        message = msg_pickle

        msg_length = len(msg_pickle)
        send_length = str(msg_length).encode('utf-8')
        # Pads message length to make sure it folows the HEADER/FORMAT of 64 in this case.
        send_length += b' ' * (HEADER - len(send_length))
        self.client.send(send_length)
        self.client.send(message)

        if msg == DISCONNECT_MESSAGE:
            self.connected = False
