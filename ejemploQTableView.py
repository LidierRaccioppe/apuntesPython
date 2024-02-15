import sys

from PyQt6 import QtGui
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout, QComboBox,
                             QWidget, QCheckBox, QHBoxLayout, QLineEdit, QTableView)
from PyQt6.QtCore import Qt, QAbstractTableModel

class ModeloTabla(QAbstractTableModel):
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla # Se almacena la tabla en un atributo de la clase
    # Métodos abstractos que deben implementarse
    def rowCount(self, indice): # Devuelve el número de filas de la tabla
        return len(self.tabla)
    def columnCount(self, indice): # Devuelve el número de columnas de la tabla
        return len(self.tabla[0])
    def data(self, indice, rol): # Devuelve el dato que se encuentra en el índice de la tabla
        if indice.isValid(): # Si el índice es válido
            if rol == Qt.ItemDataRole.EditRole or rol == Qt.ItemDataRole.DisplayRole: # Si el rol es de edición o visualización de datos de la tabla
                valor = self.tabla[indice.row()][indice.column()] # Se obtiene el valor de la tabla
                return valor
            if rol == Qt.ItemDataRole.ForegroundRole:
                if self.tabla[indice.row()][3]==True:
                    return QtGui.QColor("red")
            if rol == Qt.ItemDataRole.BackgroundRole:
                if self.tabla[indice.row()][2]=="Hombre":
                    return QtGui.QColor("green")
                if self.tabla[indice.row()][2]=="Mujer":
                    return QtGui.QColor("pink")
                if self.tabla[indice.row()][2]=="Otros":
                    return QtGui.QColor("purple")
            if rol == Qt.ItemDataRole.DecorationRole:
                if isinstance(self.tabla[indice.row()][indice.column()], bool):
                    if self.tabla[indice.row()][indice.column()]:
                        return QtGui.QIcon("check.png")

    def setData(self, indice, valor, rol): # Establece el dato en el índice de la tabla
        if rol == Qt.ItemDataRole.EditRole: # Si el rol es de edición de datos de la tabla
            self.tabla[indice.row()][indice.column()] = valor # Se establece el valor en la tabla
            return True # Se devuelve True para indicar que se ha establecido el valor
        return False # Se devuelve False para indicar que no se ha establecido el valor
    def flags(self, indice): # Devuelve los flags de edición de la tabla
        if indice.row() == 0:
            return Qt.ItemFlag.ItemIsEnabled
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable # Se devuelven los flags de edición de la tabla

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        # Inicializa la clase base QMainWindow
        super().__init__()
        self.setWindowTitle("Ejemplo QTableView con Qt") # Establece el título de la ventana
        self.datos=[["Nombre", "Dni", "Genero", "Fallecido"],
               ["Ana Pérez","12345678Y","Mujer",True],
               ["Luis González","87654321K","Hombre",False],
               ["María Sánchez","87654891H","Mujer",False],
               ["Jorge Ruíz","32754981U","Hombre",True],
               ]

        cajaV=QVBoxLayout()
        self.tvwTabla = QTableView() # Creación de la vista de la tabla
        modelo = ModeloTabla(self.datos) # Creación del modelo de datos de la tabla
        self.tvwTabla.setModel(modelo) # Configuración del modelo de datos de la tabla
        self.seleccion= self.tvwTabla.selectionModel()
        self.seleccion.selectionChanged.connect(self.on_filaSeleccionada)
        self.tvwTabla.setSelectionMode(QTableView.SelectionMode.SingleSelection)
        if self.datos is not None:
            self.tvwTabla.selectRow(1)
        cajaV.addWidget(self.tvwTabla)
        cajaH=QHBoxLayout()
        cajaV.addLayout(cajaH)
        self.txtNombre=QLineEdit("Nombre")
        cajaH.addWidget(self.txtNombre)
        self.txtDni=QLineEdit("DNI")
        cajaH.addWidget(self.txtDni)
        self.cmbGenero=QComboBox()
        self.cmbGenero.addItems(('Hombre', 'Mujer', 'Otros'))

        cajaH.addWidget(self.cmbGenero)
        self.chkFallecido=QCheckBox('Fallecido')
        cajaH.addWidget(self.chkFallecido)

        print(self.tvwTabla.selectRow(0))


        self.tvwTabla.selectRow(1)
        self.on_filaSeleccionada()



        componentePrincipal=QWidget()
        componentePrincipal.setLayout(cajaV)
        self.setCentralWidget(componentePrincipal) # Configuración de la vista de la tabla como widget central

        # Configuración del tamaño fijo de la ventana y visualización
        self.setFixedSize(400, 400)
        self.show()

    def on_filaSeleccionada(self):
        indices= self.tvwTabla.selectedIndexes()
        if indices != []:
            print(indices)
            self.txtNombre.setText(self.datos[indices[0].row()][0])
            self.txtDni.setText(self.datos[indices[0].row()][1])
            self.cmbGenero.setCurrentText(self.datos[indices[0].row()][2])
            self.chkFallecido.setChecked(self.datos[indices[0].row()][3])


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    aplicacion.exec()