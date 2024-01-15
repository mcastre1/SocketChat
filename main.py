import sys
from PyQt5.QtWidgets import QApplication, QTextEdit, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget


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

        # Creating a vertical layout, and giving it to central widget
        layout = QVBoxLayout(central_widget)

        # Creating the Textbox where we see all messages
        text_screen = QTextEdit()
        text_screen.setReadOnly(True)  # We set the text_screen as read only
        text_screen.setWordWrapMode(1)  # Set WordWrap mode (1: WrapAnywhere)

        cursor = text_screen.textCursor()
        cursor.movePosition(cursor.End)
        text_screen.setTextCursor(cursor)

        layout.addWidget(text_screen, stretch=7)

        # Creating the Text box for sending messages
        text_input = QTextEdit()
        text_screen.setWordWrapMode(1)

        layout.addWidget(text_input, stretch=1)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
