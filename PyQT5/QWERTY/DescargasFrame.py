import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon, QPixmap

class Descarga(QMainWindow):

    __captcha__ = ""
    __fechaInicio__ = ""
    __fechaFin__ = ""
    __path__ = ""
    __emiRec__ = ""

    def __init__(self, parent=None):
        super(Descarga,self).__init__(parent)        
        loadUi('templates/Captcha.ui',self)
        with open("estilos.css") as f:
            self.setStyleSheet(f.read())
        self.btn_ok.clicked.connect(self.verificaCaptcha)
        pixmap = QPixmap('../png/captcha.png')
        self.label_img.setPixmap(pixmap)
        
        
    def inicializaParams(self,fechaInicio,fechaFin,er,path):
        self.__fechaInicio__ = fechaInicio
        self.__fechaFin__ = fechaFin
        self.__emiRec__ = er
        self.__path__ = path


    def verificaCaptcha(self): 
        self.__captcha__ = self.lineEdit_cap.text()
        print(self.__captcha__)
        if (self.__captcha__ == ""):
            self.label_captcha.setStyleSheet('color: red')
            self.label_captcha.setText("¡Escriba el captcha!")
        else:
            print("Ddescargando ....")
            pass

         