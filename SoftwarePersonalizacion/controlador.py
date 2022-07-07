from asyncio.windows_events import NULL
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
import time

import gestorHotkeys as gh
import conexiondb as db
from parche import cargarperfiles
from sVentana import App2
import json

usu_sel = ''
perfil_sel = ''

# https://es.acervolima.com/como-crear-una-tecla-de-acceso-rapido-en-python/

class MyWindow(QtWidgets.QMainWindow):

    def post_usu(self):
        users = []
        users_ints = db.obtenerUsuarios()
        print(users_ints[1])
        for user in users_ints:
            users.append(str(user[1]))
        return users


    def __init__(self):
        super(MyWindow,self).__init__()
        uic.loadUi('mainv2.ui',self)    
        
        self.fill_combobox()

        self.pb_btn1.clicked.connect(self.grabar1)     #ADD Condiciones del mantener
        self.pb_btn2.clicked.connect(self.grabar2)
        self.pb_btn3.clicked.connect(self.grabar3)
        self.pb_btn4.clicked.connect(self.grabar4)
        self.pb_btn1b.clicked.connect(self.grabar1b)
        self.pb_btn2b.clicked.connect(self.grabar2b)
        self.pb_btn3b.clicked.connect(self.grabar3b)
        self.pb_btn4b.clicked.connect(self.grabar4b)
        self.pb_sw1.clicked.connect(self.grabarSW1)
        self.pb_sw2.clicked.connect(self.grabarSW2)
        self.pb_sw3.clicked.connect(self.grabarSW3)
        self.pb_sw1b.clicked.connect(self.grabarSW1b)
        self.pb_sw2b.clicked.connect(self.grabarSW2b)
        self.pb_sw3b.clicked.connect(self.grabarSW3b)
        self.pb_pv1.clicked.connect(self.grabarPV1)
        self.pb_pv2.clicked.connect(self.grabarPV2)
        self.pb_pv3.clicked.connect(self.grabarPV3)
        self.pb_pv4.clicked.connect(self.grabarPV4)
        self.pb_pv5.clicked.connect(self.grabarPV5)
        self.pb_pv6.clicked.connect(self.grabarPV6)
        self.pb_pr1.clicked.connect(self.grabarPR1)
        self.pb_pr2.clicked.connect(self.grabarPR2)
        self.pb_pr3.clicked.connect(self.grabarPR3)
        self.pb_pr4.clicked.connect(self.grabarPR4)
        self.pb_pr5.clicked.connect(self.grabarPR5)
        self.pb_pr6.clicked.connect(self.grabarPR6)

        self.btn_Mapeo.clicked.connect(self.llama)

        self.btn_export.clicked.connect(self.guardar_config)
        self.btn_import.clicked.connect(self.cargar_config)
        self.btn_eliminar.clicked.connect(self.eliminar_config)
        
        self.cb_usuario.currentIndexChanged.connect(self.actualizarperfiles)
        
        #self.btn_eliminar_usu.clicked.connect(self.borrarUsu(usu)) #ESTOY CON MI HERMMANO AUN
        
    def fill_combobox(self):
        usus = self.post_usu()
        self.cb_usuario.clear()
        self.cb_usuario.addItems(usus)
        usuario_selec = self.cb_usuario.currentText()
        usu_sel = usuario_selec
        self.cargarperfiles(usuario_selec)

    def actualizarperfiles(self):
        usuario_selec = self.cb_usuario.currentText()
        usu_sel = usuario_selec
        self.cargarperfiles(usuario_selec)

    def cargarBotones(perfiles_ints):
        for perfil in perfiles_ints:
                if(perfil == perfiles_ints[1]):
                    perfil_sel = perfil[0]
        if(perfil_sel != NULL):
            botones = db.obtenerBotones(usu_sel, perfil_sel)
            print(botones)

    def cargarperfiles(self, usu):
        perfiles = []
        usus = db.obtenerUsuarios()
        for user in usus:
            if(usu == user[1]):
                usuario = user[0]
                print(usuario)
                usu_sel = usuario
        perfiles_ints = db.obtenerPerfiles(str(usuario))
        print("Perfil select")
        print(perfiles_ints)

        self.cb_perfil.clear()
        if(len(perfiles_ints)):
            for perfil in perfiles_ints:
                print(str(perfil[2]))
                perfiles.append(str(perfil[2]))
                print(perfiles) 
            self.cb_perfil.addItems(perfiles)
            self.cargarBotones(perfiles_ints)


    def crearUsuario():
        name = "pepito"
        db.crearUsuario(name)
    
    def crearPerfil():
        name = "pepito"
        db.crearPerfil(name, usu_sel)
        

    def llama(self):
        self.app2 = QApplication(sys.argv)
        self.ui = App2()
        self.ui.initUI()
        #sys.exit(self.app2.exec_())

    def teclaPress(self):
        reply = gh.changecolor("w")
        if(reply == "rojo"):
            self.lbl_BP1.setStyleSheet("background-color : yellow")
            time.sleep(0.2)
            self.lbl_BP1.setStyleSheet("background-color : white")
       
        
    def grabar1(self):
        atajo = gh.record_hotkeys()
        self.lbl_btn1.setText(atajo)
    
    def grabar1b(self):
        atajo = gh.record_hotkeys()
        self.lbl_btn1b.setText(atajo)
    
    def grabar2(self):
        atajo = gh.record_hotkeys()
        self.lbl_btn2.setText(atajo)
    
    def grabar2b(self):
        atajo = gh.record_hotkeys()
        self.lbl_btn2b.setText(atajo)
    
    def grabar3(self):
        atajo = gh.record_hotkeys()
        self.lbl_btn3.setText(atajo)
    
    def grabar3b(self):
        atajo = gh.record_hotkeys()
        self.lbl_btn3b.setText(atajo)
    
    def grabar4(self):
        atajo = gh.record_hotkeys()
        self.lbl_btn4.setText(atajo)
    
    def grabar4b(self):
        atajo = gh.record_hotkeys()
        self.lbl_btn4b.setText(atajo)

    def grabarSW1(self):
        atajo = gh.record_hotkeys()
        self.lbl_sw1.setText(atajo)
    
    def grabarSW1b(self):
        atajo = gh.record_hotkeys()
        self.lbl_sw1b.setText(atajo)
    
    def grabarSW2(self):
        atajo = gh.record_hotkeys()
        self.lbl_sw2.setText(atajo)
    
    def grabarSW2b(self):
        atajo = gh.record_hotkeys()
        self.lbl_sw2b.setText(atajo)
    
    def grabarSW3(self):
        atajo = gh.record_hotkeys()
        self.lbl_sw3.setText(atajo)
    
    def grabarSW3b(self):
        atajo = gh.record_hotkeys()
        self.lbl_sw3b.setText(atajo)

    def grabarPV1(self):
        atajo = gh.record_hotkeys()
        self.lbl_pv1.setText(atajo)
    
    def grabarPV2(self):
        atajo = gh.record_hotkeys()
        self.lbl_pv2.setText(atajo)
    
    def grabarPV3(self):
        atajo = gh.record_hotkeys()
        self.lbl_pv3.setText(atajo)
    
    def grabarPV4(self):
        atajo = gh.record_hotkeys()
        self.lbl_pv4.setText(atajo)
    
    def grabarPV5(self):
        atajo = gh.record_hotkeys()
        self.lbl_pv5.setText(atajo)
    
    def grabarPV6(self):
        atajo = gh.record_hotkeys()
        self.lbl_pv6.setText(atajo)

    def grabarPR1(self):
        atajo = gh.record_hotkeys()
        self.lbl_pr1.setText(atajo)
    
    def grabarPR2(self):
        atajo = gh.record_hotkeys()
        self.lbl_pr2.setText(atajo)
    
    def grabarPR3(self):
        atajo = gh.record_hotkeys()
        self.lbl_pr3.setText(atajo)
    
    def grabarPR4(self):
        atajo = gh.record_hotkeys()
        self.lbl_pr4.setText(atajo)
    
    def grabarPR5(self):
        atajo = gh.record_hotkeys()
        self.lbl_pr5.setText(atajo)
    
    def grabarPR6(self):
        atajo = gh.record_hotkeys()
        self.lbl_pr6.setText(atajo)
    


    def save_config(self):
        json_filename = "./salida_btn.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump([], f)
        with open(json_filename, 'r', encoding='utf-8') as f:
            perfil = json.load(f) #Generar un json con (ids | nombres | Atajo (comandos) | mantener)

        ids = []
        ids.append("lbl_btn1")
        ids.append("lbl_btn2")
        ids.append("lbl_btn3")
        ids.append("lbl_btn4")
        ids.append("lbl_sw1")
        ids.append("lbl_sw2")
        ids.append("lbl_sw3")
        ids.append("lbl_btn1b")
        ids.append("lbl_btn2b")
        ids.append("lbl_btn3b")
        ids.append("lbl_btn4b")
        ids.append("lbl_sw1b")
        ids.append("lbl_sw2b")
        ids.append("lbl_sw3b")
        ids.append("lbl_pv1")
        ids.append("lbl_pv2")
        ids.append("lbl_pv3")
        ids.append("lbl_pv4")
        ids.append("lbl_pv5")
        ids.append("lbl_pv6")
        ids.append("lbl_pr1")
        ids.append("lbl_pr2")
        ids.append("lbl_pr3")
        ids.append("lbl_pr4")
        ids.append("lbl_pr5")
        ids.append("lbl_pr6")


        comandos = [] #controles de label
        comandos.append(self.lbl_btn1.text())
        comandos.append(self.lbl_btn2.text())
        comandos.append(self.lbl_btn3.text())
        comandos.append(self.lbl_btn4.text())
        comandos.append(self.lbl_sw1.text())
        comandos.append(self.lbl_sw2.text())
        comandos.append(self.lbl_sw3.text())
        comandos.append(self.lbl_btn1b.text())
        comandos.append(self.lbl_btn2b.text())
        comandos.append(self.lbl_btn3b.text())
        comandos.append(self.lbl_btn4b.text())
        comandos.append(self.lbl_sw1b.text())
        comandos.append(self.lbl_sw2b.text())
        comandos.append(self.lbl_sw3b.text())
        comandos.append(self.lbl_pv1.text())
        comandos.append(self.lbl_pv2.text())
        comandos.append(self.lbl_pv3.text())
        comandos.append(self.lbl_pv4.text())
        comandos.append(self.lbl_pv5.text())
        comandos.append(self.lbl_pv6.text())
        comandos.append(self.lbl_pr1.text())
        comandos.append(self.lbl_pr2.text())
        comandos.append(self.lbl_pr3.text())
        comandos.append(self.lbl_pr4.text())
        comandos.append(self.lbl_pr5.text())
        comandos.append(self.lbl_pr6.text())

        
        nombres = [] #controles de text edit
        nombres.append(self.te_btn1.toPlainText())
        nombres.append(self.te_btn2.toPlainText())
        nombres.append(self.te_btn3.toPlainText())
        nombres.append(self.te_btn4.toPlainText())
        nombres.append(self.te_sw1.toPlainText())
        nombres.append(self.te_sw2.toPlainText())
        nombres.append(self.te_sw3.toPlainText())
        nombres.append(self.te_btn1b.toPlainText())
        nombres.append(self.te_btn2b.toPlainText())
        nombres.append(self.te_btn3b.toPlainText())
        nombres.append(self.te_btn4b.toPlainText())
        nombres.append(self.te_sw1b.toPlainText())
        nombres.append(self.te_sw2b.toPlainText())
        nombres.append(self.te_sw3b.toPlainText())
        nombres.append(self.te_pv1.toPlainText())
        nombres.append(self.te_pv2.toPlainText())
        nombres.append(self.te_pv3.toPlainText())
        nombres.append(self.te_pv4.toPlainText())
        nombres.append(self.te_pv5.toPlainText())
        nombres.append(self.te_pv6.toPlainText())
        nombres.append(self.te_pr1.toPlainText())
        nombres.append(self.te_pr2.toPlainText())
        nombres.append(self.te_pr3.toPlainText())
        nombres.append(self.te_pr4.toPlainText())
        nombres.append(self.te_pr5.toPlainText())
        nombres.append(self.te_pr6.toPlainText())
        
        mantener = []
        mantener.append(self.ch_btn1.isChecked())
        mantener.append(self.ch_btn2.isChecked())
        mantener.append(self.ch_btn3.isChecked())
        mantener.append(self.ch_btn4.isChecked())
        mantener.append(self.ch_sw1.isChecked())
        mantener.append(self.ch_sw2.isChecked())
        mantener.append(self.ch_sw3.isChecked())

        for i, id in enumerate(ids):
            if (i < 7):
                entry = {
                    'position': id,
                    'name': nombres[i],
                    'shortcut': comandos[i],
                    'mantener': 0 if mantener[i] == False else 1
                }
                perfil.append(entry)
            else:
                entry = {
                    'position': ids[i],
                    'name': nombres[i],
                    'shortcut': comandos[i],
                    'mantener': 0
                }
                perfil.append(entry)

        print(perfil)
        
        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(perfil, f, ensure_ascii=False)
        return perfil

    def guardar_config(self):
        print("Se ha guardado la configuracion")
        perfil = self.save_config()
        id_profile = 1
        db.guardarBotones(id_profile)
        QtWidgets.QMessageBox.information(self, "confirmation", "Se ha guardado la configuracion")

    def cargar_config(self):
        print("Se ha cargado la configuracion")

        self.lbl_btn1.setText("btn4b")
        self.lbl_btn2.setText("btn4b")
        self.lbl_btn3.setText("btn4b")
        self.lbl_btn4.setText("btn4b")
        self.lbl_btn1b.setText("btn4b")
        self.lbl_btn2b.setText("btn4b")
        self.lbl_btn3b.setText("btn4b")
        self.lbl_btn4b.setText("btn4b")
        self.lbl_sw1.setText("sw3")
        self.lbl_sw2.setText("sw3")
        self.lbl_sw3.setText("sw3")
        self.lbl_sw1b.setText("sw2")
        self.lbl_sw2b.setText("sw3")
        self.lbl_sw3b.setText("sw3")
        self.lbl_pv1.setText("pv6")
        self.lbl_pv2.setText("pv6")
        self.lbl_pv3.setText("pv6")
        self.lbl_pv4.setText("pv6")
        self.lbl_pv5.setText("pv6")
        self.lbl_pv6.setText("pv6")
        self.lbl_pr1.setText("pr3")
        self.lbl_pr2.setText("pr3")
        self.lbl_pr3.setText("pr3")
        self.lbl_pr4.setText("pr4")
        self.lbl_pr5.setText("pr5")
        self.lbl_pr6.setText("pr6")

        QtWidgets.QMessageBox.information(self, "confirmation", "Se ha cargado la configuracion")

    def eliminar_config(self):
        print("Se ha intentado eliminar una configuración")
        reply = QtWidgets.QMessageBox.question(self, 'Confirmation windows', '¿Seguro que quieres eliminar la configuracion?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        
        print(reply)
        if reply == QtWidgets.QMessageBox.Yes:
            print("Se ha eliminado la configuracion")

            self.lbl_btn1.setText("")
            self.lbl_btn2.setText("")
            self.lbl_btn3.setText("")
            self.lbl_btn4.setText("")
            self.lbl_btn1b.setText("")
            self.lbl_btn2b.setText("")
            self.lbl_btn3b.setText("")
            self.lbl_btn4b.setText("")
            self.lbl_sw1.setText("")
            self.lbl_sw2.setText("")
            self.lbl_sw3.setText("")
            self.lbl_sw1b.setText("")
            self.lbl_sw2b.setText("")
            self.lbl_sw3b.setText("")
            self.lbl_pv1.setText("")
            self.lbl_pv2.setText("")
            self.lbl_pv3.setText("")
            self.lbl_pv4.setText("")
            self.lbl_pv5.setText("")
            self.lbl_pv6.setText("")
            self.lbl_pr1.setText("")
            self.lbl_pr2.setText("")
            self.lbl_pr3.setText("")
            self.lbl_pr4.setText("")
            self.lbl_pr5.setText("")
            self.lbl_pr6.setText("")


            db.borrarPerfil(perfil_sel)
            
        else: 
            print("No se ha eliminado la configuracion")
    
    def borrarPerfil():
        reply = QtWidgets.QMessageBox.question(self, 'Confirmation windows', '¿Seguro que quieres eliminar el perfil?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            print("Se ha eliminado la configuracion")
            db.borrarPerfil(perfil_sel)
        else: 
            print("No se ha eliminado la configuracion")

    def borrarUsu():
        reply = QtWidgets.QMessageBox.question(self, 'Confirmation windows', '¿Seguro que quieres eliminar el usuario?', QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            print("Se ha eliminado la configuracion")
            db.borrarUsuario(usu_sel)
        else: 
            print("No se ha eliminado la configuracion")
    
    

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

