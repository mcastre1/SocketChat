from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication
import sys
import mysql.connector
import hashlib
from hash import Hash


class LoginScreen(QWidget):
    def __init__(self, callback_user_info):
        super().__init__()
        self.callback_user_info = callback_user_info

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

        password = Hash.hash_sha256(password)

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
        SELECT users.user_no
        FROM users
        JOIN accounts ON users.user_no = accounts.user_no
        WHERE accounts.account_name = %s AND accounts.password = %s
        """
        # Execute the query above.
        cursor.execute(query, (username, password))

        success = False
        user_no = 0

        for row in cursor:
            user_no = int(row[0])
            success = True

        # Replace the following condition with your actual login logic
        if success:
            QMessageBox.information(
                self, "Login Successful", "Welcome, {}".format(username))
            self.callback_user_info(user_no)
            db_connection.close()
        else:
            QMessageBox.warning(self, "Login Failed",
                                "Invalid username or password")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    login_page = LoginScreen()
    login_page.show()

    sys.exit(app.exec_())
