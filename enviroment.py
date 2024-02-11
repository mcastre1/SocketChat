from PyQt5.QtWidgets import QDesktopWidget

# Returns tuple of current window centers as x and y coordinates.
def get_window_centers():
    screen_centerx, screen_centery = QDesktopWidget().availableGeometry(
        ).center().x(), QDesktopWidget().availableGeometry().center().y()
    
    return (screen_centerx, screen_centery)