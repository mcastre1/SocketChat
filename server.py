import socket
import threading
from Message import Message
import pickle

# Keep track of connections
clients = set()

# Function used to start listening for new connections
users = set()


def start(server):

    server.listen()
    print("[LISTENING] Server Listening for new connections.")

    # When a new connection is found, we create a thread and assign it to the handle_client function.
    while True:
        conn, addr = server.accept()
        clients.add(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        # This is to show how many connections are currently active.
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1} ")


# Function used to handle interaction between each client and server.
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)

        # We check if theres an actual message being received before we try to format it.
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length)

            # Here we convert the bytes from pickle into the actual Message object.
            msg = pickle.loads(msg)

            # This is where we check to see if client wants to disconnect
            if msg.msg == DISCONNECT_MESSAGE:
                # Here we will have to send in the length of the object first so we can receive the entire message correctly
                message = Message("Disconnected", "Server", "Client")
                msg_pickled = pickle.dumps(message)
                msg_length = len(msg_pickled)
                send_length = str(msg_length).encode('utf-8')
                send_length += b' ' * (HEADER - len(send_length))

                conn.send(send_length)
                conn.send(msg_pickled)

                clients.remove(conn)
                connected = False
            else:
                for client in clients:
                    # Here we do whatever we need to save for future reference, instead of on other clients iterations.
                    if client == conn:  # Also add an and to check for certain new connection message.
                        msg_pickled = pickle.dumps(msg)
                        # Might need to change message object to keep track of user number so its easier to retrieve.
                        users.add(msg.msg)

                    elif not client == conn:
                        msg_pickled = pickle.dumps(msg)
                        msg_length = len(msg_pickled)
                        send_length = str(msg_length).encode('utf-8')
                        send_length += b' ' * (HEADER - len(send_length))

                        client.send(send_length)
                        client.send(msg_pickled)

            print(f"[{addr}] {msg.msg}")

    # Close connection when we jump off the while loop
    conn.close()


HEADER = 64
PORT = 65432
ADDRESS = socket.gethostbyname(socket.gethostname())

ADDR = (ADDRESS, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'

# server = socket.
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(ADDR)
start(server)
