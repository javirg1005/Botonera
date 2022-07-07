import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
import time
import gestorHotkeys as gh
import keyboard

class App2(QtWidgets.QMainWindow):
 
    def initUI(self):
        self.setWindowTitle(self.title)
        # Create Widget 2
        pixmap = QPixmap('imagen1.jpg').scaledToHeight(530)
        self.imagen_lbl.setPixmap(pixmap)
 
        self.show()
        
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Segunda interfaz"))
    
    
    def teclaPress(self):
        parar = False
        if(parar == False):
            '''presion = gh.record_hotkeys()
            print(presion)'''
            presion = gh.getPressKeys()
            
            if(presion[0] > 0):
                self.lbl_BP1.setStyleSheet("background-color : red")
            if(self.btn_ST.clicked):
                parar = True
   
    def __init__(self):
        #super().__init__()
        super(App2,self).__init__()
        self.title = 'Guía de botonera'
        uic.loadUi('.\imagen.ui',self)    
        self.initUI()

        self.btn_ST.clicked.connect(self.teclaPress)


if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App2()
        sys.exit(app.exec_())
