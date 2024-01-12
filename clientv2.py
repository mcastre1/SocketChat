import socket
import threading


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


def receive():
    global connected
    while connected:
        print(client.recv(2048).decode(FORMAT))


def send():
    global connected
    while connected:
        msg = input(":")
        message = msg.encode(FORMAT)  # Encode into byte format first.

        msg_length = len(msg)
        send_length = str(msg_length).encode('utf-8')
        # Pads message length to make sure it folows the HEADER/FORMAT of 64 in this case.
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
        # print(client.recv(2048).decode(FORMAT))

        if msg == DISCONNECT_MESSAGE:
            connected = False


# This is so I can talk to the server without having to close and open multiple times.
sending = threading.Thread(target=send)
sending.start()
receiving = threading.Thread(target=receive)
receiving.start()
