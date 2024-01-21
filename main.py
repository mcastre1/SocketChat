from login_window import LoginScreen
import sys
from PyQt5.QtWidgets import QApplication


class SocketChat(QApplication):
    def __init__(self):
        super().__init__(sys.argv)

        # Login Screen.
        login_screen = LoginScreen()
        login_screen.show()

        # We need this to keep the application from closing
        # and only closing when we actually close the window.
        sys.exit(self.exec_())


if __name__ == "__main__":
    # app = QApplication(sys.argv)

    # login_screen = LoginScreen()
    # login_screen.show()

    # sys.exit(app.exec_())

    app = SocketChat()
