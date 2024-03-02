class Message:
    def __init__(self, msg, sender, recipient):
        self.msg = msg
        self.sender = sender
        self.recipient = recipient


class NewConnection:
    def __init__(self, msg, sender_id, recipient, sender_name):
        self.msg = msg
        self.sender_id = sender_id
        self.sender_name = sender_name
        self.recipient = recipient
