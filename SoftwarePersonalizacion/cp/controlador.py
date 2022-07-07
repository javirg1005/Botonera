import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import time

import gestorHotkeys as gh
import conexiondb as db
from sVentana import App2
import json

perfiles = []
usuarios = []

# https://es.acervolima.com/como-crear-una-tecla-de-acceso-rapido-en-python/

class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow,self).__init__()
        uic.loadUi('.\main.ui',self)    
        
        self.btn_eliminar_usu.clicked.connect(self.borrarUsu())
        self.btn_eliminar_perfil.clicked.connect(self.borrarPerfil())

        self.pushButton.clicked.connect(self.grabar)
        self.pushButton_2.clicked.connect(self.grabar2)
        self.pushButton_3.clicked.connect(self.grabar3)
        self.pushButton_4.clicked.connect(self.grabar4)
        self.pushButton_5.clicked.connect(self.grabar5)
        self.pushButton_6.clicked.connect(self.grabar6)
        self.pushButton_7.clicked.connect(self.grabar7)
        self.pushButton_8.clicked.connect(self.grabar8)
        self.btn_SW1.clicked.connect(self.llama)
        self.btn_SW2.clicked.connect(self.popWindow) #Añadir un evento de clic para el botón

        self.btn_export.clicked.connect(self.guardar_config)
        self.btn_import.clicked.connect(self.cargar_config)
        self.btn_eliminar.clicked.connect(self.eliminar_config)
        

    def llama(self):
        self.app2 = QApplication(sys.argv)
        self.ui = App2()
        self.ui.initUI()

    def teclaPress(self):
        reply = gh.changecolor("w")
        if(reply == "rojo"):
            self.lbl_BP1.setStyleSheet("background-color : yellow")
            time.sleep(0.2)
            self.lbl_BP1.setStyleSheet("background-color : white")
       

    def popWindow(self):
        self.form2 = QtWidgets.QWidget() 
        self.ui2 = App2()
        #self.ui2.setupUi(self.form2)
        self.form2.show() 
    
        
    def grabar(self):
        atajo = gh.record_hotkeys()
        self.label.setText(atajo)
    
    def grabar2(self):
        atajo = gh.record_hotkeys()
        self.label_2.setText(atajo)
    
    def grabar3(self):
        atajo = gh.record_hotkeys()
        self.label_3.setText(atajo)
    
    def grabar4(self):
        atajo = gh.record_hotkeys()
        self.label_4.setText(atajo)
    
    def grabar5(self):
        atajo = gh.record_hotkeys()
        self.label_5.setText(atajo)

    def grabar6(self):
        atajo = gh.record_hotkeys()
        self.label_6.setText(atajo)
    
    def grabar7(self):
        atajo = gh.record_hotkeys()
        self.label_7.setText(atajo)
    
    def grabar8(self):
        atajo = gh.record_hotkeys()
        self.label_8.setText(atajo)

    def save_config(self):
        perfil = [] #Generar un json con (ID | Nombre | tecla)
        comandos = [] #controles de label
        comandos.append(self.label.text())
        comandos.append(self.label_2.text())
        comandos.append(self.label_3.text())
        comandos.append(self.label_4.text())
        comandos.append(self.label_5.text())
        comandos.append(self.label_6.text())
        comandos.append(self.label_7.text())
        comandos.append(self.label_8.text())
        
        nombres = [] #controles de text edit
        nombres.append(self.textEdit.toPlainText())
        nombres.append(self.textEdit_2.toPlainText())
        nombres.append(self.textEdit_3.toPlainText())
        nombres.append(self.textEdit_4.toPlainText())
        nombres.append(self.textEdit_5.toPlainText())
        nombres.append(self.textEdit_6.toPlainText())
        nombres.append(self.textEdit_7.toPlainText())
        nombres.append(self.textEdit_8.toPlainText())
        
        mantener = []
        mantener.append(self.ch_1.isChecked())
        mantener.append(self.ch_2.isChecked())
        mantener.append(self.ch_3.isChecked())
        mantener.append(self.ch_4.isChecked())
        mantener.append(self.ch_5.isChecked())
        mantener.append(self.ch_6.isChecked())
        mantener.append(self.ch_7.isChecked())
        mantener.append(self.ch_8.isChecked())
        
        perfil.append(comandos)
        perfil.append(nombres)
        perfil.append(mantener)
        print(perfil)
        return perfil

    def guardar_config(self):
        print("Se ha guardado la configuracion")
        perfil = self.save_config()
        QtWidgets.QMessageBox.information(self, "confirmation", "Se ha guardado la configuracion")

    def cargar_config(self):
        print("Se ha cargado la configuracion")
        QtWidgets.QMessageBox.information(self, "confirmation", "Se ha cargado la configuracion")

    def eliminar_config(self):
        print("Se ha intentado eliminar una configuración")
        reply = QtWidgets.QMessageBox.question(self, 'Confirmation windows', '¿Seguro que quieres eliminar la configuracion?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        
        print(reply)
        if reply == QtWidgets.QMessageBox.Yes:
            print("Se ha eliminado la configuracion")
            self.label.setText("")
            self.label_2.setText("")
            self.label_3.setText("")
            self.label_4.setText("")
            self.label_5.setText("")
            self.label_6.setText("")
            self.label_7.setText("")
            self.label_8.setText("")
            
        else: 
            print("No se ha eliminado la configuracion")
    
    def borrarPerfil():
        reply = QtWidgets.QMessageBox.question(self, 'Confirmation windows', '¿Seguro que quieres eliminar el perfil?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            print("Se ha eliminado la configuracion")
            db.borrarPerfil(perfiles)
        else: 
            print("No se ha eliminado la configuracion")

    def borrarUsu():
        reply = QtWidgets.QMessageBox.question(self, 'Confirmation windows', '¿Seguro que quieres eliminar el usuario?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            print("Se ha eliminado la configuracion")
            db.borrarUsuario(usuarios)
        else: 
            print("No se ha eliminado la configuracion")
    


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

