from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication
import sys


class LoginScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)

        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        login_button = QPushButton("Login")
        login_button.clicked.connect(self.check_login)
        layout.addWidget(login_button)

        self.setLayout(layout)

    def check_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        # Replace the following condition with your actual login logic
        if username == "user" and password == "password":
            QMessageBox.information(
                self, "Login Successful", "Welcome, {}".format(username))
        else:
            QMessageBox.warning(self, "Login Failed",
                                "Invalid username or password")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_page = LoginScreen()
    login_page.show()

    sys.exit(app.exec_())
