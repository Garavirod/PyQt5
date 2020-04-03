import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel, QMessageBox
from PyQt5.uic import loadUi
from DescargasFrame import Descarga

class ParametrosWindow(QMainWindow):
    __fechaInicio__ = ""
    __fechaFin__ = ""
    __rutaDescarga__ = ""
    __emitReci__ = ""
    __detalle__ = """
        ¿Desea proceder con la siguiente descarga?\n\n 
            1. Ruta descarga : {} \n 
            2. Feha inicio :  {} \n 
            3. Fecha fin : {} \n 
            4. E/R : {}"""

    def __init__(self, parent=None):
        super(ParametrosWindow,self).__init__(parent)
        loadUi('templates/Parametros.ui',self)        
        self.btn_ok.clicked.connect(self.enviaCampos)
        self.btn_ruta.clicked.connect(self.seleccionaruta)
        self.btn_cerrar.clicked.connect(self.cierraApp)
        self.combo.addItems(['Emitidas','Recibidas'])        

    def cierraApp(self):
        self.close()

    def enviaCampos(self):        
        if(self.__rutaDescarga__ != ""):
            self.__fechaInicio__ = (self.fecha_from.date()).toPyDate()
            self.__fechaFin__ = (self.fecha_to.date()).toPyDate()
            self.__emitReci__ = self.combo.currentText()
            _download = Descarga(self)        
            _download.inicializaParams(self.__fechaInicio__,self.__fechaFin__,self.__emitReci__,self.__rutaDescarga__)              
            resp = QMessageBox.question(self,'Detalle de descarga',self.__detalle__.format(self.__rutaDescarga__,self.__fechaInicio__,self.__fechaFin__,self.__emitReci__), QMessageBox.Ok | QMessageBox.Cancel)
            if(resp == QMessageBox.Ok):
                print("Descarga confrimada")
                _download.show()
        else:  
            QMessageBox.information(self, 'Parametros faltantes', "¡Olvidates colocar ruta de descarga!", QMessageBox.Ok)

                                  
    def seleccionaruta(self):
        self.__rutaDescarga__ = str(QFileDialog.getExistingDirectory(self))
        self.scroll.setWidget(QLabel(self.__rutaDescarga__))        