import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import uic
import time
#import gestorHotkeys as gh

class App2(QtWidgets.QMainWindow):
 
    def __init__(self):
        #super().__init__()
        super(App2,self).__init__()
        self.title = 'Guía de botonera'
        #self.left = 20
        #self.top = 20
        #self.width = 640
        #self.height = 480
        uic.loadUi('.\imagenV2.ui',self)    
        self.initUI()

        #self.btn_ST.clicked.connect(self.teclaPress())

    def initUI(self):
        self.setWindowTitle(self.title)
        #self.setGeometry(self.left, self.top, self.width, self.height)

        '''
        # Create widget
        label = QLabel(self)
        pixmap = QPixmap('imagen.jpg')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(),pixmap.height())
        '''
        # Create Widget 2

        pixmap = QPixmap('imagen.jpg')
        self.imagen_lbl.setPixmap(pixmap)
 
        self.show()
        
    

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Segunda interfaz"))
    
    '''
    def teclaPress(self):
        parar = False
        while(parar == False):
            reply = gh.changecolor2("w")
            if(reply == "rojo"):
                self.lbl_BP1.setStyleSheet("background-color : yellow")
                time.sleep(0.2)
                self.lbl_BP1.setStyleSheet("background-color : white")
            if(self.btn_ST.clicked):
                parar = True
   '''



if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = App2()
        sys.exit(app.exec_())
