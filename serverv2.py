import socket
import threading

# Function used to start listening for new connections.


def start(server):
    server.listen()

    # When a new connection is found, we create a thread and assign it to the handle_client function.
    while True:
        conn, addr = server.accept()
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
            msg = conn.recv(msg_length).decode(FORMAT)

            # This is where we check to see if client wants to disconnect
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

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
