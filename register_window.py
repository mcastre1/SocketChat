from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton, QDesktopWidget
import sys
import mysql.connector


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()

    # Creates all ui components in the register window.
    def ui_init(self):
        # Geometry of screen to make sure it appears at the center of current screen.
        self.screen_centerx, self.screen_centery = QDesktopWidget().availableGeometry(
        ).center().x(), QDesktopWidget().availableGeometry().center().y()
        self.height = 150
        self.width = 300

        # Title of screen and size
        self.setWindowTitle('Register')
        self.setGeometry(self.screen_centerx - self.width/2,
                         self.screen_centery - self.height/2, self.width, self.height)

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

        cursor = db_connection.cursor()

        try:
            insert_query = "INSERT INTO users (name, email) VALUES (%s, %s)"
            insert_data = (self.name_input.text(), self.email_input.text())

            cursor.execute(insert_query, insert_data)

            last_inserted_id = cursor.lastrowid

            insert_query = ("INSERT INTO accounts "
                            "(account_name, password, user_no)"
                            "VALUES (%s, %s, %s)")

            insert_data = (self.account_input.text(),
                           self.password_input.text(), last_inserted_id)

            cursor.execute(insert_query, insert_data)
        except:
            print("Error")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    register_window = RegisterWindow()
    register_window.show()

    sys.exit(app.exec_())