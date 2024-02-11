from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDesktopWidget
import sys
import mysql.connector
from hash import Hash
from Validation import Validation
from Popup import Popup
from enviroment import get_window_centers


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()

    # Creates all ui components in the register window.
    def ui_init(self):
        # Geometry of screen to make sure it appears at the center of current screen.
        self.screen_centerx, self.screen_centery = get_window_centers()
        self.height = 150
        self.width = 300

        # Title of screen and size
        self.setWindowTitle('Register')
        self.setGeometry(self.screen_centerx - int(self.width/2),
                         self.screen_centery - int(self.height/2), self.width, self.height)

        # Vertical layout
        layout = QVBoxLayout()

        # Adding bouth ui components for the users account name
        self.account_label = QLabel("Account:")
        self.account_input = QLineEdit()

        layout.addWidget(self.account_label)
        layout.addWidget(self.account_input)

        # Adding bouth ui components for the users password.
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        # Used to hide password and convert into * characters on textbox.
        self.password_input.setEchoMode(QLineEdit.Password)

        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)

        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()

        # Adding both ui components for the Users name
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        # Adding both ui components for the Users email
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        self.register_button = QPushButton('Register')
        self.register_button.clicked.connect(self.new_user)

        layout.addWidget(self.register_button)

        # Setting this QWidget layout to the one with the added widgets above.
        self.setLayout(layout)

    def new_user(self):
        # Connect to db
        db_connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mc255587!",
            database='socketchat'
        )

        # Cursor to execute queries
        cursor = db_connection.cursor()

        # Validation of fields
        email_validated = Validation.validate_email(self.email_input.text())
        account_validated = Validation.validate_account(
            self.account_input.text())
        name_validated = Validation.validate_name(self.name_input.text())
        password_validated = Validation.validate_password(
            self.password_input.text())

        # Validation messages
        val_message = ""
        print(email_validated)
        print(account_validated)
        print(name_validated)
        print(password_validated)

        if not account_validated:
            val_message = val_message + "Account not valid.\n"
        if not password_validated:
            val_message = val_message + "Password not valid.\n"
        if not name_validated:
            val_message = val_message + "Name not valid.\n"
        if not email_validated:
            val_message = val_message + "Email not valid.\n"

        if email_validated and account_validated and name_validated and password_validated:
            # Using try except to make sure theres no problems on database side.
            try:
                # Creating a new row in users
                insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
                insert_data = (self.name_input.text(), self.email_input.text())

                cursor.execute(insert_query, insert_data)

                # Keeping track of the new users id
                last_inserted_id = cursor.lastrowid

                # Use new user id as foreign key to create a new account.
                insert_query = ("INSERT INTO accounts "
                                "(account_name, password, user_no)"
                                "VALUES (%s, %s, %s)")

                insert_data = (self.account_input.text(),
                               Hash.hash_sha256(self.password_input.text()), last_inserted_id)

                cursor.execute(insert_query, insert_data)
                db_connection.commit()
                db_connection.close()
            except:
                print("Error")
        else:
            # Popup window with messages.
            popup = Popup("Something went wrong", val_message)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    register_window = RegisterWindow()
    register_window.show()

    sys.exit(app.exec_())
