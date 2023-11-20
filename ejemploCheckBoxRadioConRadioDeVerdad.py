import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QCheckBox, \
    QRadioButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

contador = 0
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QCheckBox y QRadioButton")

        cajaV=QVBoxLayout()

        self.chkBoton1 = QCheckBox ("Boton 1")
        self.chkBoton1.toggled.connect(self.on_chkBoton1_toggled)
        cajaV.addWidget(self.chkBoton1)


        self.chkBoton2 = QCheckBox ("Boton 2")
        self.chkBoton2.toggled.connect(self.on_chkBoton2_toggled)
        cajaV.addWidget(self.chkBoton2)

        cajaV2 = QVBoxLayout()
        contenedorV2 = QWidget()
        contenedorV2.setLayout(cajaV2)
        cajaV.addWidget(contenedorV2)

        # Para agrupar un boton
        self.rbtRadioBoton1 = QRadioButton("Opcion 1", contenedorV2)
        self.rbtRadioBoton1.toggled.connect(self.on_rbtRadioBoton1_toggled)
        cajaV2.addWidget(self.rbtRadioBoton1)

        # Para agrupar otro boton
        self.rbtRadioBoton2 = QRadioButton("Opcion 2", contenedorV2)
        self.rbtRadioBoton2.toggled.connect(self.on_rbtRadioBoton2_toggled)
        cajaV2.addWidget(self.rbtRadioBoton2)

        # Para agrupar otro boton
        self.rbtRadioBoton3 = QRadioButton("Opcion 3", contenedorV2)
        self.rbtRadioBoton3.toggled.connect(self.on_rbtRadioBoton3_toggled)
        cajaV2.addWidget(self.rbtRadioBoton3)

        # Para agrupar 3 nuevos botones en una nueva caja
        cajaV3 = QVBoxLayout()
        contenedorV3 = QWidget()
        contenedorV3.setLayout(cajaV3)
        cajaV.addWidget(contenedorV3)

        self.rbtRadioBoton4 = QRadioButton("Opcion 4", contenedorV3)
        # Cada boton tiene su propio metodo
        self.rbtRadioBoton4.toggled.connect(self.on_rbtRadioBoton4_toggled)
        cajaV3.addWidget(self.rbtRadioBoton4)

        self.rbtRadioBoton5 = QRadioButton("Opcion 5", contenedorV3)
        self.rbtRadioBoton5.toggled.connect(self.on_rbtRadioBoton5_toggled)
        cajaV3.addWidget(self.rbtRadioBoton5)

        self.rbtRadioBoton6 = QRadioButton("Opcion 6", contenedorV3)
        self.rbtRadioBoton6.toggled.connect(self.on_rbtRadioBoton6_toggled)
        cajaV3.addWidget(self.rbtRadioBoton6)

        self.chkBoton3 = QRadioButton("Boton 1")

        
        contenedor = QWidget()

        contenedor.setLayout(cajaV)


        self.setCentralWidget(contenedor)

        self.setFixedSize(400, 300)
        self.show()
    def on_rbtRadioBoton1_toggled(self):
        if self.rbtRadioBoton1.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton1.text())
        else:
            print("Check Boton deseleccionado"+ self.rbtRadioBoton1.text())
    def on_rbtRadioBoton2_toggled(self):
        if self.rbtRadioBoton2.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton2.text())
        else:
            print("Check Boton deseleccionado"+ self.rbtRadioBoton2.text())
    def on_rbtRadioBoton3_toggled(self):
        if self.rbtRadioBoton3.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton3.text())
        else:
            print("Check Boton deseleccionado"+ self.rbtRadioBoton3.text())
    def on_rbtRadioBoton4_toggled(self):
        if self.rbtRadioBoton4.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton4.text())
        else:
            print("Check Boton deseleccionado"+ self.rbtRadioBoton4.text())
    def on_rbtRadioBoton5_toggled(self):
        if self.rbtRadioBoton5.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton5.text())
        else:
            print("Check Boton deseleccionado"+ self.rbtRadioBoton5.text())
    def on_rbtRadioBoton6_toggled(self):
        if self.rbtRadioBoton6.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton6.text())
        else:
            print("Check Boton deseleccionado"+ self.rbtRadioBoton6.text())
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
