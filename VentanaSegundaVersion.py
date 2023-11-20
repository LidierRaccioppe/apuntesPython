import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

contador = 0
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mi primera ventana - fiestra es en gallego con Qt")

        self.txtSaludo = QLineEdit()
        self.txtSaludo.editingFinished.connect(self.presionasEnter)
        self.lblEtiqueta1 = QLabel("Hola a los presentes")

        ## no funciona :   self.txtSaludo.returnPressed.connect(self.lblEtiqueta1.setText) # de esta forma no tenemos que crear un metodo pero solo mete el texto
        fuente = self.lblEtiqueta1.font()
        fuente.setPointSize(30)


        """
        self.lblEtiqueta2 = QLabel("Mi mama dice que soy especial")
        self.lblEtiqueta2.setPixmap(QPixmap("giu.png"))
        """
        self.btnSaludo = QPushButton("Saludo")
        self.btnSaludo.clicked.connect(self.on_btnSaludo_clicked)

        self.cajaV = QVBoxLayout()
        self.cajaV.addWidget(self.lblEtiqueta1)
        # self.cajaV.addWidget(self.lblEtiqueta2)
        self.cajaV.addWidget(self.txtSaludo)
        self.cajaV.addWidget(self.btnSaludo)


        contenedor = QWidget()
        contenedor.setLayout(self.cajaV)


        self.setCentralWidget(contenedor)

        self.setFixedSize(400, 300)
        self.show()
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
