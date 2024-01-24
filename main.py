from login_window import LoginScreen
import sys
from PyQt5.QtWidgets import QApplication
from chat_window import ChatWindow


class SocketChat(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        # Login Screen.
        self.login_screen = LoginScreen(self.create_chat_window)
        self.login_screen.show()

        self.chat_screen = None

        # We need this to keep the application from closing
        # and only closing when we actually close the window.
        sys.exit(self.exec_())

    def create_chat_window(self, user_no):
        # Close login screen once there is succesful login.
        self.login_screen.close()
        self.chat_screen = ChatWindow(user_no)
        self.chat_screen.show()
        print(user_no)


if __name__ == "__main__":
    app = SocketChat()
