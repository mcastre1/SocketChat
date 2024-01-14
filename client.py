import socket
import threading
import pickle
from Message import Message


HEADER = 64
# Which port should the server use, 5050 just because. Use something is not being used for something else.
PORT = 65432
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# Address of server, for now its the local ip address of machine we are running the server in
SERVER = "192.168.86.95"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Socket connects requires a tuple of server address, port.
client.connect(ADDR)

connected = True

# We receive and print all messages from server here.


def receive():
    global connected
    while connected:
        msg_length = client.recv(HEADER).decode(FORMAT)

        if msg_length:
            msg_length = int(msg_length)
            msg = client.recv(msg_length)

            msg = pickle.loads(msg)

            print(msg.msg)


def send(name):
    global connected
    while connected:
        msg = input(":")
        msg_object = Message(msg, "", "")
        msg_pickle = pickle.dumps(msg_object)
        message = msg_pickle

        msg_length = len(msg_pickle)
        send_length = str(msg_length).encode('utf-8')
        # Pads message length to make sure it folows the HEADER/FORMAT of 64 in this case.
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)

        if msg == DISCONNECT_MESSAGE:
            connected = False


# This is so I can talk to the server without having to close and open multiple times.
# name = input("Name: ")

sending = threading.Thread(target=send, args=[""])
sending.start()
receiving = threading.Thread(target=receive)
receiving.start()
