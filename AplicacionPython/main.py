from tkinter import *
import tkinter
from tkinter import messagebox
import serial

# Global variables
closeArduino = False
arduinoFind = False
# Funciones
def on_closing():    
    if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas cerrar esta ventana?"):
        global closeArduino
        closeArduino = True
        mainWindow.destroy()
        if(arduinoFind):
            arduino.close()
        print("SE CIERRA LA COMUNICACION")

# Inicializacion de la ventana
mainWindow = tkinter.Tk()
#Variables
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
coeffScreenSize = 0.7

# Configuración de la ventana
mainWindow.geometry(str(int(screen_width*coeffScreenSize)) + "x" + str(int(screen_height*coeffScreenSize)))
mainWindow.title("ECG y SpO2")
mainWindow.configure(bg="#abebc6")

# Widgets
label = tkinter.Label(mainWindow)
label.pack()

#Events Handlers
mainWindow.protocol("WM_DELETE_WINDOW", on_closing)
# Bucle de la ventana
while(True):
    if(closeArduino):
        break
    if(not arduinoFind):
        try: 
            # Comunicación serie con el arduino
            arduino = serial.Serial("COM5",9600)
        except serial.SerialException as e:
            label["text"] = "CONECTE SU ARDUINO"
            pass
        else:
            arduinoFind = True
            pass
    else:
        try:
            val = arduino.readline()
            valDecode = val.decode("ascii")
            label["text"] = valDecode
        except serial.SerialException as e:
            label["text"] = "PARECE QUE SU ARDUINO SE DESCONECTO. INTENTE CONECTARLO NUEVAMENTE"
            arduinoFind = False
            pass
    mainWindow.update()