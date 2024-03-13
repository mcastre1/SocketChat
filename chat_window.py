import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QSizePolicy, QMessageBox, QLabel
from client import Client
import mysql.connector
from Message import NewConnection, Message


class ChatWindow(QMainWindow):
    def __init__(self, user_no):
        super(ChatWindow, self).__init__()
        self.user_no = user_no

        self.user_name = self.get_user_name()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 400)
        self.ui()

        self.client = Client()
        self.client.upate_text.connect(self.append_text)
        self.client.update_client_list.connect(self.update_client_list)
        self.client.run()

        self.send_message(f"Connection from ID: {self.user_no}", NewConnection)

    def get_user_name(self):
        # Connect to db
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mc255587!",
            database='socketchat'
        )

        cursor = db_connection.cursor()

        # Call DB account table and retrieve user number on succesful login
        query = """
        SELECT name
        FROM users
        WHERE user_no = %s
        """
        # Execute the query above.
        cursor.execute(query, [self.user_no])

        user_name = None

        for row in cursor:
            user_name = row[0]

        return user_name

    # Update the current connected clients list.
    def update_client_list(self, conn_dict):
        # First we clear out the text
        self.clients_text.setPlainText("")

        # Then we append all the user names in connections
        for key in conn_dict.keys():
            user_name = conn_dict[key][0]
            self.clients_text.setPlainText(
                self.clients_text.toPlainText() + f"\n{user_name}")

    def ui(self):
        # Creating the central area for widgets to live in main window.
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        # This layout is in charge of all layouts.
        self.main_layout = QHBoxLayout(central_widget)

        self.left_layout = QVBoxLayout()
        self.right_layout = QVBoxLayout()

        # Creating a vertical layout for the top part.
        self.top_layout = QVBoxLayout()

        # Creating the Textbox where we see all messages
        self.text_screen = QTextEdit()
        # We set the text_screen as read only
        self.text_screen.setReadOnly(True)
        # Set WordWrap mode (1: WrapAnywhere)
        self.text_screen.setWordWrapMode(1)

        # This will keep the text at the bottom of textbox
        cursor = self.text_screen.textCursor()
        cursor.movePosition(cursor.End)
        self.text_screen.setTextCursor(cursor)

        self.top_layout.addWidget(self.text_screen)

        # Creating a horizontal layout for the bottom part of the app.
        bottom_layout = QHBoxLayout()

        # Creating the Text box for sending messages
        self.text_input = QTextEdit()
        self.text_input.setWordWrapMode(1)

        bottom_layout.addWidget(self.text_input, stretch=7)

        # And the button for sending said messages.
        button_send = QPushButton('Send')
        bottom_layout.addWidget(button_send, stretch=1)
        button_send.clicked.connect(
            lambda: self.send_message(self.text_input.toPlainText(), Message))

        # Set the size policy for the button to expanding for both width and height
        size_policy = button_send.sizePolicy()
        size_policy.setHorizontalPolicy(QSizePolicy.Expanding)
        size_policy.setVerticalPolicy(QSizePolicy.Expanding)
        button_send.setSizePolicy(size_policy)

        # Adding both top and bottom layouts with their respective widgets to left layout.
        self.left_layout.addLayout(self.top_layout, stretch=7)
        self.left_layout.addLayout(bottom_layout, stretch=1)

        # Creating the Textbox where we see all messages
        self.clients_text = QTextEdit()
        # We set the text_screen as read only
        self.clients_text.setReadOnly(True)
        # Set WordWrap mode (1: WrapAnywhere)
        self.clients_text.setWordWrapMode(1)

        self.right_layout.addWidget(self.clients_text)

        # Adding left and right layouts to main layout.
        self.main_layout.addLayout(self.left_layout, stretch=7)
        self.main_layout.addLayout(self.right_layout, stretch=1)

    def send_message(self, msg, msg_type):
        if msg_type == Message:
            msg = msg.strip()  # Get rid of trailing/leading whitespace
            self.client.send(msg=msg, sender=self.user_name,
                             message_type=Message)

            self.text_screen.setPlainText(
                self.text_screen.toPlainText() + f"\nYou: {msg}")

            self.text_input.setText("")
        elif msg_type == NewConnection:
            msg = msg.strip()
            self.client.send(msg=msg, sender=self.user_no,
                             message_type=NewConnection, sender_name=self.user_name)

    # Appends the received text to the text box on the left layout.
    def append_text(self, msg):
        if not isinstance(msg, NewConnection):
            msg.msg = msg.msg.strip()  # Get rid of trailing/leading whitespace
            self.text_screen.setPlainText(
                self.text_screen.toPlainText() + f"\n{msg.sender}:{msg.msg}")

    def closeEvent(self, event):
        # Define your custom logic here
        reply = QMessageBox.question(self, 'Confirmation', 'Are you sure you want to log out?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.send_message("!DISCONNECT", msg_type=Message)
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ChatWindow("1")
    main_window.show()
    sys.exit(app.exec_())
