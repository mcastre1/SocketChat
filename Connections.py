class Connections:
    def __init__(self):
        self.connections = {}

    def add_connection(self, user_id, conn):
        self.connections[user_id] = conn

    def remove_connection(self, user_id):
        del self.connections[user_id]
