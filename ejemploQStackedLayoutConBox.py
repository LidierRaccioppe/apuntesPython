import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, \
    QHBoxLayout, QGridLayout, QStackedLayout

from cajaColor import CajaColor

class GridConContenido(QGridLayout):
    def __init__(self):
        super().__init__()

        self.addWidget(CajaColor("red"))
        self.addWidget(CajaColor("blue"), 0, 1, 1, 2)
        self.addWidget(CajaColor("green"), 1, 0, 2, 1)
        self.addWidget(CajaColor("pink"), 1, 1, 1, 2)
        self.addWidget(CajaColor("orange"), 2, 1, 1, 1)
        self.addWidget(CajaColor("yellow"), 2, 2, 1, 1)

class HBoxModifcadoColor(QHBoxLayout):
    def __init__(self):
        super().__init__()
        caja1 = QVBoxLayout()
        caja3 = QVBoxLayout()

        caja1.addWidget(CajaColor("red"))
        caja1.addWidget(CajaColor("yellow"))
        caja1.addWidget(CajaColor("purple"))
        self.addLayout(caja1)

        self.addWidget(CajaColor("green"))

        caja3.addWidget(CajaColor("blue"))
        caja3.addWidget(CajaColor("orange"))
        self.addLayout(caja3)
class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QStacked Layout con Qt")

        cajaBotonesH = QHBoxLayout()
        cajaV = QVBoxLayout()
        cajaV.addLayout(cajaBotonesH)
        self.tarjetas = QStackedLayout()
        cajaV.addLayout(self.tarjetas)


        btnRojo = QPushButton("Que Este Rojo")
        btnRojo.pressed.connect(self.on_btnRojo_pressed)
        cajaBotonesH.addWidget(btnRojo)

        btnAzul = QPushButton("Que Este Azul")
        btnAzul.pressed.connect(self.on_btnAzul_pressed)
        cajaBotonesH.addWidget(btnAzul)

        btnMalla = QPushButton("Que Este Malla")
        btnMalla.pressed.connect(self.on_btnMalla_pressed)
        cajaBotonesH.addWidget(btnMalla)

        btnBModificado = QPushButton("Que Este Box")
        btnBModificado.pressed.connect(self.on_btnBModificado_pressed)
        cajaBotonesH.addWidget(btnBModificado)

        ## Los indices se agregan empezando en 0
        
        self.tarjetas.addWidget(CajaColor("red"))
        self.tarjetas.addWidget(CajaColor("blue"))

        widgedGrid = QWidget()
        widgedGrid.setLayout(GridConContenido())
        self.tarjetas.addWidget(widgedGrid)


        widgedBox = QWidget()
        widgedBox.setLayout(HBoxModifcadoColor())
        self.tarjetas.addWidget(widgedBox)

        control = QWidget()


        control.setLayout(cajaV)
        self.setCentralWidget(control)
        self.show()



    def on_btnRojo_pressed(self):
        self.tarjetas.setCurrentIndex(0)

    def on_btnAzul_pressed(self):
        self.tarjetas.setCurrentIndex(1)

    def on_btnMalla_pressed(self):
        self.tarjetas.setCurrentIndex(2)

    def on_btnBModificado_pressed(self):
        self.tarjetas.setCurrentIndex(3)



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = FiestraPrincipal()
    aplicacion.exec()