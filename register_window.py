from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit, QPushButton
import sys


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui_init()

    # Creates all ui components in the register window.
    def ui_init(self):
        # Title of screen and size
        self.setWindowTitle('Register')
        self.setGeometry(100, 100, 300, 150)

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

        layout.addWidget(self.register_button)

        # Setting this QWidget layout to the one with the added widgets above.
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    register_window = RegisterWindow()
    register_window.show()

    sys.exit(app.exec_())
