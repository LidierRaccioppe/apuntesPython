import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

contador = 0
class CajaColor (QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window,QColor(color))
        self.setPalette(paleta)