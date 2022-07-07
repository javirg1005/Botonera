import serial, time
import keyboard, pynput
ard = serial.Serial('COM4',9600)


while 1:
    datos = ard.readline().decode('ascii')
    print(datos)
    dato1, dato2 = datos.split(',')
    print(dato1)
    print(dato2)
    if int(dato1) < 50:
        #keyboard("arrow_up")
        key = 'A'
        keyboard.press(key)
    if int(dato1) > 50:
        print('BAJAA')


