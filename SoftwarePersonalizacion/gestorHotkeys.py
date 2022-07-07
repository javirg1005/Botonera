import time
import keyboard
import re

#Arduino
import serial, time
#ard = serial.Serial('COM4',9600)

def record_hotkey():    #grabar hotkey
  	#show key
    a = keyboard.read_key()
    print(a)
	#reset show()
    if keyboard != "":
        time.sleep(0.1)
        #record_hotkey() #bucle
        return a

def record_hotkeys():    #grabar hotkeys
  	#show key
    time.sleep(0.1)
    a = keyboard.read_key()
    print(a)
	#reset show()
    if a != (""):
        time.sleep(0.1)
        coso = ["ctrl","alt","shift","left windows","right alt",""]
        if(a in coso):
            print("Siguiente tecla")
            a = a +"+"+ record_hotkeys() #bucle
            return a
        else:
            return a

def changecolor(tecla):
    salida = False
    while(salida == False):
        red = "rojo"
        time.sleep(0.1)
        if(keyboard.read_key() == tecla):
            #return red
            print(red)
        else:
            print("nada")
        
def changecolor2(teclapress, tecla):
    red = "rojo"
    time.sleep(0.1)
    if(teclapress == tecla):
        #return red
        print(red)
        return red
    else:
        print("nada")
        return "nada"
        
#Coger datos arduino
def getPressKeys():
    datos = ard.readline().decode()
    #.decode('utf-8')
    #dato_array = datos.split('\n')
    print(datos)
    datos = str(datos)
    dato_array = re.sub('[^0-9,]+', '', datos)
    
    print(dato_array)
    dato_array = dato_array.split(',')
    
    print(dato_array)
    dato_array = dato_array[:-2]
    print(dato_array)
    dato_array_int = [ìnt(x) for x in dato_array]
    return 