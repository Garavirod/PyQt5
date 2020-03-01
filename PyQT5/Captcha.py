from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi

class CaptchaWindow(QMainWindow):
    def __init__(self, parent=None):
        super(CaptchaWindow,self).__init__(parent)
        loadUi('Captcha.ui',self)
        self.btn_ok.clicked.connect(self.verificaCaptcha)
        self.btn_recap.clicked.connect(self.generaNuevoCaptcha)

    def verificaCaptcha(Self): 
         pass   
        # Validar si el capctha no fue correcto  
        # if True:
        #     self.label_captcha.setStyleSheet('color: red')
        #     self.label_captcha.setText("¡El captcha no coincide!")
        # else:
        #     # De ser correcto mostrar un emergente con la leyenda de exito
        #     # y mostrar la ruta donde se guardó
         
    def generaNuevoCaptcha(self):
        pass