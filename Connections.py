class Connections:
    def __init__(self):
        self.connections = {}

    def add_connection(self, user_id, user_name, addr):
        self.connections[user_id] = [user_name, addr]

    def remove_connection(self, user_id):
        del self.connections[user_id]

    def get_connections(self) -> dict:
        return self.connections
