import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, \
    QHBoxLayout, QGridLayout

from cajaColor import CajaColor

class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo Grid Layout con Qt")

        malla = QGridLayout()


        malla.addWidget(CajaColor("red"))
        malla.addWidget(CajaColor("blue"), 0, 1, 1, 2)
        malla.addWidget(CajaColor("green"), 1, 0, 2, 1)
        malla.addWidget(CajaColor("pink"), 1, 1, 1, 2)
        malla.addWidget(CajaColor("orange"), 2, 1, 1, 1)
        malla.addWidget(CajaColor("yellow"), 2, 2, 1, 1)


        control = QWidget()

        control.setLayout(malla)
        self.setCentralWidget(control)
        self.show()



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = FiestraPrincipal()
    aplicacion.exec()