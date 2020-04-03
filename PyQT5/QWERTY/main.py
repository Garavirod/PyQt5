from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from Parametros import ParametrosWindow

class VentanaPrincipal(QMainWindow):
    __user__ ="1"
    __pass__ ="1"
    def __init__(self):
        super(VentanaPrincipal,self).__init__()
        loadUi('templates/Credenciales.ui',self)       
        self.btn_ok.clicked.connect(self.validaCredenciales)
        self.btn_cerrar.clicked.connect(self.cierraApp)

    def cierraApp(self):
        self.close()

    def validaCredenciales(self):
        user = self.lineEdit_User.text()
        password = self.lineEdit_password.text()
        if (user == "" or password=="" ):
            self.label_credencial.setStyleSheet('color: orange')
            self.label_credencial.setText("¡Hay Campos vacios!")
        elif (user==self.__user__) and (password==self.__pass__):
            parametros = ParametrosWindow(self)
            parametros.show()
            self.hide()
        else:
            self.label_credencial.setStyleSheet('color: red')
            self.label_credencial.setText("¡contraseña o usuario incorrecto!")


if __name__ == "__main__":
    app = QtWidgets.QApplication([]) #Permite controlar el bucle del programa
    window = VentanaPrincipal()
    window.show()
    app.exec_() #El programa se cerrará inmediatemente al no estar esta linea
