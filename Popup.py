from PyQt5.QtWidgets import QMessageBox


class Popup:
    def __init__(self, title, message):
        self.show_popup_message(title, message)

    def show_popup_message(self, title, message):

        message_box = QMessageBox()
        message_box.setWindowTitle(title)
        message_box.setText(message)

        # Optional
        message_box.setIcon(QMessageBox.Information)

        # Buttons
        message_box.setDefaultButton(QMessageBox.Ok)

        message_box.exec_()
