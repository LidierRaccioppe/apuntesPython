import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QHBoxLayout
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtCore import Qt

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

        self.cajaHGrande = QHBoxLayout()

        self.cajaVPrimer = QVBoxLayout()
        self.lblEtiqueta3 =QLabel("etiqueta 3")
        self.cajaVPrimer.addWidget(self.lblEtiqueta3)
        self.lblEtiqueta4 =QLabel("etiqueta 4")
        self.cajaVPrimer.addWidget(self.lblEtiqueta4)
        self.lblEtiqueta5 =QLabel("etiqueta 5")
        self.cajaVPrimer.addWidget(self.lblEtiqueta5)
        self.cajaHGrande.addLayout(self.cajaVPrimer)

        self.cajaVSegunda = QVBoxLayout()
        self.lblEtiqueta6 =QLabel("etiqueta 6")
        self.cajaVSegunda.addWidget(self.lblEtiqueta6)
        self.cajaHGrande.addLayout(self.cajaVSegunda)



        self.cajaVTercera = QVBoxLayout()
        self.lblEtiqueta7 =QLabel("etiqueta 7")
        self.cajaVTercera.addWidget(self.lblEtiqueta7)
        self.lblEtiqueta8 =QLabel("etiqueta 8")
        self.cajaVTercera.addWidget(self.lblEtiqueta8)
        self.cajaHGrande.addLayout(self.cajaVTercera)

        contenedor = QWidget()
        contenedor.setLayout(self.cajaHGrande)


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

class CajaColor (QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window,QColor(color))
        self.setPalette(paleta)

class VentanaVentanante(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Aplicacion con Box Boxeante")
        contenedor = QHBoxLayout()
        caja1 = QHBoxLayout()
        caja2 = QHBoxLayout()

        caja1.addWidget(CajaColor("red"))
        caja1.addWidget(CajaColor("yellow"))
        caja1.addWidget(CajaColor("purple"))
        contenedor.addWidget(caja1)

        caja2.addWidget(CajaColor("blue"))
        caja2.addWidget(CajaColor("orange"))
        contenedor.addWidget(caja2)


        self.setCentralWidget(QWidget().setLayout(contenedor))





if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()