import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from Captcha import CaptchaWindow

class ParametrosWindow(QMainWindow):
    def __init__(self, parent=None):
        super(ParametrosWindow,self).__init__(parent)
        loadUi('Parametros.ui',self)
        self.btn_ok.clicked.connect(self.validaCampos)
        self.btn_cerrar.clicked.connect(self.cierraApp)
        self.combo.addItems(['Emitidas','Recibidas'])

    def cierraApp(self):
        self.close()

    def validaCampos(self):
        fecha_from = (self.fecha_from.date()).toPyDate()
        fecha_to = (self.fecha_to.date()).toPyDate()
        combo = self.combo.currentText()
        print("AQUI VA EL SCRIPT DE GENERAR Y DESCARGAR DATOS")
        captcha = CaptchaWindow(self)
        captcha.show()        
