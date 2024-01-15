import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QSizePolicy


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 400)

        self.ui()

    def ui(self):
        # Creating the central area for widgets to live in main window.
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # This layout is in charge of all layouts.
        main_layout = QVBoxLayout(central_widget)

        # Creating a vertical layout for the top part.
        top_layout = QVBoxLayout()

        # Creating the Textbox where we see all messages
        text_screen = QTextEdit()
        text_screen.setReadOnly(True)  # We set the text_screen as read only
        text_screen.setWordWrapMode(1)  # Set WordWrap mode (1: WrapAnywhere)

        # This will keep the text at the bottom of textbox
        cursor = text_screen.textCursor()
        cursor.movePosition(cursor.End)
        text_screen.setTextCursor(cursor)

        top_layout.addWidget(text_screen)

        # Creating a horizontal layout for the bottom part of the app.
        bottom_layout = QHBoxLayout()

        # Creating the Text box for sending messages
        text_input = QTextEdit()
        text_input.setWordWrapMode(1)

        bottom_layout.addWidget(text_input, stretch=7)

        # And the button for sending said messages.
        button_send = QPushButton('Send')
        bottom_layout.addWidget(button_send, stretch=1)

        # Set the size policy for the button to expanding for both width and height
        size_policy = button_send.sizePolicy()
        size_policy.setHorizontalPolicy(QSizePolicy.Expanding)
        size_policy.setVerticalPolicy(QSizePolicy.Expanding)
        button_send.setSizePolicy(size_policy)

        # Adding both top and bottom layouts with their respective widgets to main layout.
        main_layout.addLayout(top_layout, stretch=7)
        main_layout.addLayout(bottom_layout, stretch=1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())