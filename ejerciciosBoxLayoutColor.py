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

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicacion con Box Boxeante")
        contenedor = QHBoxLayout()
        caja1 = QVBoxLayout()
        caja3 = QVBoxLayout()

        caja1.addWidget(CajaColor("red"))
        caja1.addWidget(CajaColor("yellow"))
        caja1.addWidget(CajaColor("purple"))
        contenedor.addLayout(caja1)

        contenedor.addWidget(CajaColor("green"))

        caja3.addWidget(CajaColor("blue"))
        caja3.addWidget(CajaColor("orange"))
        contenedor.addLayout(caja3)

        widgetP = QWidget()
        widgetP.setLayout(contenedor)
        self.setCentralWidget(widgetP)
        self.show()





if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()