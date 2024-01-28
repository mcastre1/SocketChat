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


if __name__ == '__main__':
    app = QApplication(sys.argv)

    register_window = RegisterWindow()
    register_window.show()

    sys.exit(app.exec_())
