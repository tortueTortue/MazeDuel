"""
Tools and methods
"""
import qdarkstyle
import os

from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui

def set_window_style(app: QApplication) -> None:
    """
    Sets style of a QMainWindow
    """
    QtGui.QFontDatabase.addApplicationFont('assets/fonts/UBUNTU-BOLD.ttf')
    ubuntu = QtGui.QFont('Ubuntu')
    ubuntu.setBold(True)
    app.setFont(ubuntu)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))