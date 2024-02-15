import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QLineEdit, \
    QHBoxLayout, QGridLayout, QStackedLayout, QListView
from PyQt6.QtCore import  Qt, QAbstractListModel
class TareasModelo (QAbstractListModel):
    def __init__(self, tareas=None):
        super().__init__()
        self.tareas = tareas or []
    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            estado, texto = self.tareas[indice.row()]
            return texto
        """
        Tipos de Roles:
        DisplayRole
        DecorationRole 
        """

    def rowCount(self, indice):
        return len(self.tareas)

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejemplo QListView")


        cajaVertical = QVBoxLayout()

        textoGrande = QListView()
        btnBorrar = QPushButton("Borrar")
        btnHecho = QPushButton("Hecho")
        self.lineaAgregar = QLineEdit()
        btnAnadir = QPushButton("Añadir Tarea")
        btnAnadir.pressed.connect(self.on_btnAnadir_pressed)



        listaTareas = [(False, "Una Tarea"), (False, "Segunda Tarea")]

        self.modelo = TareasModelo(listaTareas)
        textoGrande.setModel(self.modelo)
        cajaVertical.addWidget(textoGrande)

        cajaHBotonesBorrarHecho = QHBoxLayout()

        cajaHBotonesBorrarHecho.addWidget(btnBorrar)
        cajaHBotonesBorrarHecho.addWidget(btnHecho)

        cajaVertical.addLayout(cajaHBotonesBorrarHecho)
        cajaVertical.addWidget(self.lineaAgregar)
        cajaVertical.addWidget(btnAnadir)
        self.setCentralWidget(container)
        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = FiestraPrincipal()
    aplicacion.exec()