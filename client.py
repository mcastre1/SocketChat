import socket
import threading
import pickle
from Message import Message, NewConnection
from PyQt5.QtCore import pyqtSignal, QObject
from Connections import Connections

HEADER = 64
# Which port should the server use, 5050 just because. Use something is not being used for something else.
PORT = 65432
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Address of server, for now its the local ip address of machine we are running the server in
SERVER = "192.168.86.95"
ADDR = (SERVER, PORT)


class Client(QObject):
    upate_text = pyqtSignal(object)

    connections = []

    def __init__(self):
        super().__init__()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Socket connects requires a tuple of server address, port.
        self.client.connect(ADDR)

        self.connected = True

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

                print(msg)
                # If the received message is a new connection info, we dont have to display it on the text box.
                # We also do this so we dont have to check all over again every time we raise the pyqtsignal
                # if isinstance(msg, NewConnection):
                #     self.connections = msg
                #     print(f"{msg.sender_name} has logged in!")
                # Here we get all the connections received and overwrite the current list of connections
                if isinstance(msg, Connections):
                    self.connections = msg.connections
                else:
                    self.upate_text.emit(msg)

    def send(self, msg, sender, message_type, sender_name=""):
        # These if branches are to check type of messages being sent.
        if message_type == Message:
            msg_object = Message(msg, sender, "")
        elif message_type == NewConnection:
            msg_object = NewConnection(msg, sender, "Server", sender_name)

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
