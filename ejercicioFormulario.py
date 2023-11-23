import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, QCheckBox, \
    QRadioButton, QHBoxLayout, QListView, QComboBox, QGridLayout, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

contador = 0


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QCheckBox y QRadioButton")

        ## La principal
        cajaVPrincipal = QVBoxLayout()


        ## Con tres verticales
        cajaHPrincipal1 = QHBoxLayout()
        cajaVSecundaria1 = QVBoxLayout()
        ## La base para las de disco (imagen) y el boton check
        cajaVTerciariaBase = QVBoxLayout()

        lblImagen = QLabel()
        lblImagen.setPixmap(QPixmap("giu.png"))

        cajaVTerciariaBase.addWidget(lblImagen)

        self.chkBoton2 = QCheckBox ("Animado")
        self.chkBoton2.toggled.connect(self.on_chkBoton2_toggled)
        cajaVTerciariaBase.addWidget(self.chkBoton2)

        cajaVSecundaria1.addLayout(cajaVTerciariaBase)
        cajaHPrincipal1.addLayout(cajaVSecundaria1)
        ## Caja segunda que en verdad es una QListView
        vista = QListView()
        vista.setFixedSize(400,300)
        cajaHPrincipal1.addWidget(vista)

        ## Caja tercera 3era con la los botones es una vertical
        cajaVSecundaria2 = QVBoxLayout()
        ## Agregar todos los botones que deba
        btnAñadirPista = QPushButton("Añadir a la pista a reproducir")
        cajaVSecundaria2.addWidget(btnAñadirPista)
        btnSubirEnLista = QPushButton("Subir en la lista")
        cajaVSecundaria2.addWidget(btnSubirEnLista)
        btnBajarEnLaLista = QPushButton("Bajar en la lista")
        cajaVSecundaria2.addWidget(btnBajarEnLaLista)

        btnSaltar = QPushButton("Saltar")
        combSaltar = QComboBox()

        gridSaltar = QGridLayout()
        gridSaltar.addWidget(btnSaltar,0,0)
        gridSaltar.addWidget(combSaltar,0,1,1,1)

        cajaVSecundaria2.addLayout(gridSaltar)
        btnAbrirArchivo = QPushButton("Abrir Archivo")
        cajaVSecundaria2.addWidget(btnAbrirArchivo)
        btnReproducirArchivo = QPushButton("Reproducir Archivo")
        cajaVSecundaria2.addWidget(btnReproducirArchivo)
        btnGuardarComo = QPushButton("GuardarComo")
        cajaVSecundaria2.addWidget(btnGuardarComo)
        btnEliminarPista = QPushButton("EliminarPista")
        cajaVSecundaria2.addWidget(btnEliminarPista)

        cajaHPrincipal1.addLayout(cajaVSecundaria2)
        cajaVPrincipal.addLayout(cajaHPrincipal1)
        cajaHPrincipal2 = QHBoxLayout()

        gridSonido = QGridLayout()
        cajaHPrincipal2.addLayout(gridSonido)
        lblSondio = QLabel("Sonido: ")
        lblRitmo = QLabel("Ritmo: ")
        lblVolumen = QLabel("Volumen: ")
        lblFormato = QLabel("Formato: ")
        lblSalidaAudio = QLabel("Salida de Audio: ")

        comSon = QComboBox()
        comRitmo = QComboBox()
        comVolumen = QComboBox()
        comFormato = QComboBox()
        comSalida = QComboBox()

        gridSonido.addItem(lblSondio,0,0,1,1)
        gridSonido.addItem(comSon,0,1,1,1)
        gridSonido.addItem(lblVolumen,1,0,1,1)
        gridSonido.addItem(lblRitmo,1,1,1,1)
        gridSonido.addItem(lblFormato,2,0,1,1)
        gridSonido.addItem(comFormato,2,1,1,1)
        gridSonido.addItem(lblSondio,3,0,1,1)
        gridSonido.addItem(comSalida,3,1,1,1)



        caja5 = QHBoxLayout()





        frmOpcRepro = QFrame()


        frmOpcRepro.setFrameStyle(QFrame.Shape.Box)


        gridReproduccion = QGridLayout()
        frmOpcRepro.setLayout(caja5)
        frmOpcRepro.setWindowTitle("Opciones de reproduccion")
        cajaHPrincipal2.addWidget(frmOpcRepro)



        cajaVPrincipal.addLayout(cajaHPrincipal2)
        contenedor = QWidget()

        contenedor.setLayout(cajaVPrincipal)

        self.setCentralWidget(contenedor)

        self.setFixedSize(800, 600)
        self.show()

    def on_rbtRadioBoton1_toggled(self):
        if self.rbtRadioBoton1.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton1.text())
        else:
            print("Check Boton deseleccionado" + self.rbtRadioBoton1.text())

    def on_rbtRadioBoton2_toggled(self):
        if self.rbtRadioBoton2.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton2.text())
        else:
            print("Check Boton deseleccionado" + self.rbtRadioBoton2.text())

    def on_rbtRadioBoton3_toggled(self):
        if self.rbtRadioBoton3.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton3.text())
        else:
            print("Check Boton deseleccionado" + self.rbtRadioBoton3.text())

    def on_rbtRadioBoton4_toggled(self):
        if self.rbtRadioBoton4.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton4.text())
        else:
            print("Check Boton deseleccionado" + self.rbtRadioBoton4.text())

    def on_rbtRadioBoton5_toggled(self):
        if self.rbtRadioBoton5.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton5.text())
        else:
            print("Check Boton deseleccionado" + self.rbtRadioBoton5.text())

    def on_rbtRadioBoton6_toggled(self):
        if self.rbtRadioBoton6.isChecked():
            print("Check Boton seleccionado: ", self.rbtRadioBoton6.text())
        else:
            print("Check Boton deseleccionado" + self.rbtRadioBoton6.text())

    def on_chkBoton1_toggled(self):
        if self.chkBoton1.isChecked():
            print("Check Boton seleccionado: ", self.chkBoton1.text())
        else:
            print("Check Boton deseleccionado" + self.chkBoton1.text())

    def on_chkBoton2_toggled(self):
        if self.chkBoton2.isChecked():
            print("Check Boton seleccionado: ", self.chkBoton2.text())
        else:
            print("Check Boton deseleccionado" + self.chkBoton2.text())

    def on_btnSaludo_clicked(self, etiqueta: QLabel, contador=None):
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
