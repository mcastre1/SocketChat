from login_window import LoginScreen
import sys
from PyQt5.QtWidgets import QApplication


class SocketChat(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        # Login Screen.
        self.login_screen = LoginScreen(self.create_chat_window)
        self.login_screen.show()

        # We need this to keep the application from closing
        # and only closing when we actually close the window.
        sys.exit(self.exec_())

    def create_chat_window(self, user_no):
        # Close login screen once there is succesful login.
        self.login_screen.close()
        print(user_no)


if __name__ == "__main__":
    app = SocketChat()
