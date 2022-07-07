import time
import keyboard

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
        
