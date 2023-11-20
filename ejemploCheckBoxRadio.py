import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QCheckBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

contador = 0
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QCheckBox")

        cajaV=QVBoxLayout()

        self.chkBoton1 = QCheckBox ("Boton 1")
        self.chkBoton1.toggled.connect(self.on_chkBoton1_toggled)
        cajaV.addWidget(self.chkBoton1)


        self.chkBoton2 = QCheckBox ("Boton 2")
        self.chkBoton2.toggled.connect(self.on_chkBoton2_toggled)
        cajaV.addWidget(self.chkBoton2)


        contenedor = QWidget()
        contenedor.setLayout(cajaV)


        self.setCentralWidget(contenedor)

        self.setFixedSize(400, 300)
        self.show()
    def on_chkBoton1_toggled(self):
        if self.chkBoton1.isChecked():
            print("Check Boton seleccionado: ", self.chkBoton1.text())
        else:
            print("Check Boton deseleccionado"+ self.chkBoton1.text())
    def on_chkBoton2_toggled(self):
        if self.chkBoton2.isChecked():
            print("Check Boton seleccionado: ", self.chkBoton2.text())
        else:
            print("Check Boton deseleccionado"+ self.chkBoton2.text())




    def on_btnSaludo_clicked(self, etiqueta : QLabel, contador=None):
        print("ajwdoinadoipnawk")
        saludo = self.txtSaludo.text()
        self.lblEtiqueta1.setText(saludo)
    def presionasEnter(self):
        saludo = self.txtSaludo.text()
        self.lblEtiqueta1.setText(saludo)

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()
