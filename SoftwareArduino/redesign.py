from nbformat import read
import serial, time
import keyboard, pynput
import json

ard = serial.Serial('COM4',9600) #Establece la conexion

#Bucle de recepcion de datos
with open('../SoftwarePersonalizacion\salida_btn.json') as file:
    acciones = json.load(file)

def haz(press,accion, position):
    if press == 0:
        #keyboard("arrow_up")
        key = accion[position]
        keyboard.press(key)
    if press == 1:
        key = accion[position]
        keyboard.press(key)

while 1:
    datos = ard.readline().decode('ascii')
    print(datos)
    senso = datos.split(',')
    if senso[0] == 0:
        haz(1,acciones[0]['shortcut'],acciones[0]['position'])
    if senso[1] == 0:
        haz(1,acciones[1]['shortcut'],acciones[1]['position'])
    if senso[2] == 0:
        haz(2,acciones[2]['shortcut'],acciones[2]['position'])
    if senso[3] == 0:
        haz(3,acciones[3]['shortcut'],acciones[3]['position'])
    if senso[4] == 0:
        haz(4,acciones[4]['shortcut'],acciones[4]['position'])
    if senso[5] == 0:
        haz(5,acciones[5]['shortcut'],acciones[5]['position'])
    if senso[6] == 0:
        haz(6,acciones[6]['shortcut'],acciones[6]['position'])
    if senso[7] == 0:
        haz(7,acciones[7]['shortcut'],acciones[7]['position'])
    if senso[8] == 0:
        haz(8,acciones[8]['shortcut'],acciones[8]['position'])
    if senso[9] == 0:
        haz(9,acciones[9]['shortcut'],acciones[9]['position'])
    if senso[10] == 0:
        haz(10,acciones[10]['shortcut'],acciones[10]['position'])
    if senso[11] == 0:
        haz(11,acciones[11]['shortcut'],acciones[11]['position'])
    if senso[12] == 0:
        haz(12,acciones[12]['shortcut'],acciones[12]['position'])
    if senso[13] == 0:
        haz(13,acciones[13]['shortcut'],acciones[13]['position'])
    if senso[14] == 0:
        haz(14,acciones[14]['shortcut'],acciones[14]['position'])
    if senso[15] == 0:
        haz(15,acciones[15]['shortcut'],acciones[15]['position'])



    