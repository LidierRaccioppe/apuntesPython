import sys  # Only needed for access to command line arguments

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget,
                             QComboBox, QFrame, QLineEdit, QGroupBox, QSlider, QListView, QListWidgetItem, QRadioButton)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Examen 27/11/2023")

        # Declaramos lo layouts principales
        layoutGeneral = QVBoxLayout()
        layoutFilaArriba = QVBoxLayout()
        layoutFilaMedio = QHBoxLayout()
        layoutFilaAbajo = QVBoxLayout()

        # Diseñamos la parte superior de la interfaz

        # Fila superior
        filaNombre = QWidget()
        filaPrim = QHBoxLayout()
        filaNombre.setLayout(filaPrim)
        nombre = QLabel("Nombre")
        cajaNombre = QLineEdit()
        cajaNombre.setPlaceholderText("")
        apellido = QLabel("Apellido")
        cajaApellido = QLineEdit()
        cajaApellido.setPlaceholderText("")
        filaPrim.addWidget(nombre)
        filaPrim.addWidget(cajaNombre)
        filaPrim.addWidget(apellido)
        filaPrim.addWidget(cajaApellido)

        layoutFilaArriba.addWidget(filaNombre)

        # Fila central
        filaTlf = QWidget()
        filaCen = QHBoxLayout()
        filaTlf.setLayout(filaCen)
        tratamiento = QLabel("Tratamiento")
        cajaTrata = QLineEdit()
        telefono = QLabel("Teléfono")
        cajaTlf = QLineEdit()
        cajaTlf.setPlaceholderText("")
        filaCen.addWidget(tratamiento)
        filaCen.addWidget(cajaTrata)
        filaCen.addWidget(telefono)
        filaCen.addWidget(cajaTlf)

        layoutFilaArriba.addWidget(filaTlf)

        # Fila inferior
        filaForma = QWidget()
        filaInf = QHBoxLayout()
        filaForma.setLayout(filaInf)
        formato = QLabel("Formato")
        comboForma = QComboBox()
        comboForma.addItems(["", "1", "2"])
        filaInf.addWidget(formato)
        filaInf.addWidget(comboForma)

        layoutFilaArriba.addWidget(filaForma)

        # PASAMOS A LA PARTE CENTRAL DE LA INTERFAZ
        parteMedio = QWidget()
        medio = QHBoxLayout()
        parteMedio.setLayout(medio)

        # Lista vertical
        # Parte de lista
        lista = QWidget()
        listaVer = QVBoxLayout()
        lista.setLayout(listaVer)
        listaCentro = QListWidget()
        listaVer.addWidget(listaCentro)

        # Parte de dirección
        direccion = QWidget()
        dirH = QHBoxLayout()
        direccion.setLayout(dirH)
        dirCorreo = QLabel("Dirección de correo")
        cajaCorreo = QLineEdit()
        dirH.addWidget(dirCorreo)
        dirH.addWidget(cajaCorreo)

        listaVer.addWidget(direccion)

        # Parte botones
        botones = QWidget()
        boton = QHBoxLayout()
        botones.setLayout(boton)
        botonAnadir = QPushButton("Añadir")
        botonEditar = QPushButton("Editar")
        botonBorrar = QPushButton("Borrar")
        botonDefault = QPushButton("Por defecto")
        boton.addWidget(botonAnadir)
        boton.addWidget(botonEditar)
        boton.addWidget(botonBorrar)
        boton.addWidget(botonDefault)

        # Funciones
        botonAnadir.clicked.connect(lambda: self.addLista(cajaNombre, cajaApellido, cajaTlf, listaCentro))
        botonAnadir.clicked.connect(lambda: self.clearCajas(cajaNombre, cajaApellido, cajaTlf))

        botonEditar.clicked.connect(lambda: self.addEditar(listaCentro, cajaNombre, cajaApellido, cajaTlf))

        listaVer.addWidget(botones)
        layoutFilaMedio.addWidget(lista)
        medio.addWidget(lista)

        # Parte de checkboxes

        correo = QWidget()
        correoVer = QVBoxLayout()
        correo.setLayout(correoVer)
        formaCorreo = QLabel("Formato de correo:")
        checkHTML = QRadioButton("HTML")
        checkPlain = QRadioButton("Texto plano")
        checkPerso = QRadioButton("Personalizado")
        correoVer.setContentsMargins(0, 0, 0, 300)
        correoVer.addWidget(formaCorreo)
        correoVer.addWidget(checkHTML)
        correoVer.addWidget(checkPlain)
        correoVer.addWidget(checkPerso)

        # Funcionalidad
        checkHTML.clicked.connect(self.mostrarRadioHTML)
        checkPlain.clicked.connect(self.mostrarRadioPlain)
        checkPerso.clicked.connect(self.mostrarRadioPers)


        medio.addWidget(correo)

        layoutFilaMedio.addWidget(parteMedio)

        # Parte inferior de la UI

        # Fila inferior
        botones2 = QWidget()
        boton2 = QHBoxLayout()
        botones2.setLayout(boton2)
        botonCancelar = QPushButton("Cancelar")
        botonAceptar = QPushButton("Aceptar")
        boton2.addWidget(botonCancelar)
        boton2.addWidget(botonAceptar)
        boton2.setContentsMargins(300, 0, 0, 0)

        botonCancelar.clicked.connect(self.cerrar)

        layoutFilaAbajo.addWidget(botones2)

        layoutGeneral.addLayout(layoutFilaArriba)
        layoutGeneral.addLayout(layoutFilaMedio)
        layoutGeneral.addLayout(layoutFilaAbajo)

        widgetLayoutGeneral = QWidget()
        widgetLayoutGeneral.setLayout(layoutGeneral)
        self.setCentralWidget(widgetLayoutGeneral)

    # FUNCIONALIDAD DE LA INTERFAZ

    # CERRAR PROGRAMA CON CANCELAR

    def cerrar(self):
        self.close()

    # MOSTRAR RADIO BUTTONS EN CONSOLA

    def mostrarRadioHTML(self):

        print("Se ha seleccionado HTML.")

    def mostrarRadioPlain(self):

        print("Se ha seleccionado texto plano.")

    def mostrarRadioPers(self):

        print("Se ha seleccionado personalizado.")

    # AÑADIR A LA LISTA NOMBRE, APELLIDO Y TELÉFONO AL PRESIONAR AÑADIR. LOS CUADROS DEBEN QUEDAR VACÍOS AL AÑADIRLO A LA LISTA.

    def addLista(self, cajaNombre, cajaApellido, cajaTlf, listaCentro):

        nombre = cajaNombre.text()
        apellido = cajaApellido.text()
        cajaTlf = cajaTlf.text()
        datos = nombre + " " + apellido + " " + cajaTlf
        listaCentro.addItem(datos)

    def clearCajas(selfs, cajaNombre, cajaApellido, cajaTlf):
        cajaNombre.clear()
        cajaApellido.clear()
        cajaTlf.clear()

    # AL PULSAR EDITAR, RECOGE EL TEXTO DE LA LISTA Y LO INCORPORA A LOS QLINE TEXT



    def addEditar (self, listaCentro, cajaNombre, cajaApellido, cajaTlf):

        elementos = listaCentro.count()

        for i in range(elementos):
            elemento=listaCentro.item(i)
            textElemento=elemento.text()
            texto = textElemento.split()

            cajaNombre.setText(texto[0])
            cajaApellido.setText(texto[1])
            cajaTlf.setText(texto[2])

            listaCentro.clear()



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
