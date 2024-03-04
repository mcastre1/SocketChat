class Connections:
    def __init__(self):
        self.connections = {}

    def add_connection(self, user_id, user_name):
        self.connections[user_id] = user_name

    def remove_connection(self, user_id):
        del self.connections[user_id]
