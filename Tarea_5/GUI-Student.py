# Utilizar QLineEdit para ingresar los datos
# Utilizar QPushButton para realizar las acciones
# Mostrar mensajes en QTextEdit (mensajes de escritura, lectura, actualización, eliminación y errores)

from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import Slot
from guistuden import Ui_MainWindow

from Mongo import Estudiantes


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.registros = []

        self.ui.Registrar.clicked.connect(self.registrar)
        self.ui.Buscar.clicked.connect(self.Buscar)
        self.ui.Eliminar.clicked.connect(self.Eliminar)
        self.ui.Actualizar.clicked.connect(self.Actualizar)
        self.ui.Limpiar.clicked.connect(self.ui.cuadro.clear)


    @Slot()
    def registrar(self):
        tmp = Estudiantes.write(self, self.ui.nombre.text(), self.ui.Email.text(), self.ui.Password.text())

        if tmp != None:
            self.ui.cuadro.append(str(tmp))

        self.ui.nombre.clear()
        self.ui.Email.clear()
        self.ui.Password.clear()

    @Slot()
    def Buscar(self):

        tmp = Estudiantes.read(self, self.ui.nombre.text())
        self.ui.cuadro.append(str(tmp))

        if self.ui.Email.text() or self.ui.Password.text():
            error = 'Busqueda solo valida por nombre... Intente de nuevo'
            self.ui.cuadro.append(str(error))

    @Slot()
    def Eliminar(self):
        temp = Estudiantes.remove(self, self.ui.nombre.text())
        self.ui.cuadro.append(str(temp))

        if self.ui.Email.text() or self.ui.Password.text():
            error = 'Eliminacion solo valida por nombre... Intente de nuevo'
            self.ui.cuadro.append(str(error))

    @Slot()
    def Actualizar(self):
        temp = Estudiantes.updates(self, self.ui.nombre.text(), self.ui.Email.text(), self.ui.Password.text())
        self.ui.cuadro.append(str(temp))


if __name__ == '__main__':
    app = QApplication()

    window = MainWindow()
    window.show()

    app.exec_()
