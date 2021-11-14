from os import read
import tkinter
import serial
from tkinter import StringVar, messagebox
from PIL import Image,ImageTk

# Global variables
titleApp = "My Heart"
closeArduino = False
arduinoFind = False
colorLightGreen = "#abebc6"
portCOM = ""
fontH1 = 'Arabic Transparent'
sizeH1 = 50
fontH2 = 'Times New Roman'
sizeH2 = 20
sizeH3 = 14
state = 1

# Funciones
def on_closing():    
    if messagebox.askokcancel("Cerrar programa", "¿Estás seguro de que deseas cerrar esta ventana?"):
        global closeArduino
        closeArduino = True
        mainWindow.destroy()
        if(arduinoFind):
            arduino.close()
        print("SE CIERRA LA COMUNICACION")

def on_changing_COM(text):
    global portCOM
    if(str.isdigit(text) or text==""):
        if(text == ""):
            return True
        else:
            if(int(text) <= 256 and int(text) > 0 and text[0] != '0'):
                portCOM = "COM" + text
                return True
            elif (int(text) == 0 and len(text) == 1):
                portCOM = "COM0"
                return True
            else:
                return False
    else:
        return False

def on_connect():
    global arduino
    global arduinoFind
    try: 
        # Comunicación serie con el arduino
        arduino = serial.Serial(portCOM,9600)
    except serial.SerialException as e:
        labelInfo["text"] = "NO SE HA PODIDO CONECTAR. VERIFIQUE SI EL PUERTO ES EL CORRECTO."
        pass
    else:
        print("CONEXION CON EXITO")
        arduinoFind = True
        dataFrame.tkraise(conectionFrame)
        pass

def UpdatePlaces1():
    midWidth = conectionFrame.winfo_width()*0.5
    midtHeight = conectionFrame.winfo_height()*0.5
    labelImgArduino.place(x=midWidth, y=midtHeight-labelImgArduino.winfo_height()*0.25)
    labelTitle.place(x=midWidth, y=midtHeight-labelImgArduino.winfo_height()*0.75-labelTitle.winfo_height()*0.5-5)
    labelInfo.place(x=midWidth, y=midtHeight+labelImgArduino.winfo_height()*0.25+labelInfo.winfo_height()*0.5+5)
    heightCOMM = midtHeight+labelImgArduino.winfo_height()*0.25+labelInfo.winfo_height()+labelCOMM.winfo_height()*0.5+10
    labelCOMM.place(x=midWidth, y=heightCOMM)
    heightEntryCOMM = heightCOMM+labelCOMM.winfo_height()*0.5+numberCOM.winfo_height()*0.5+5
    numberCOM.place(x=midWidth, y=heightEntryCOMM)
    heightButtonConnect = heightEntryCOMM+numberCOM.winfo_height()*0.5+connectbutton.winfo_height()*0.5 + 5
    connectbutton.place(x=midWidth,y=heightButtonConnect)

# Ventana principal
mainWindow = tkinter.Tk()

# Variables
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
coeffScreenSize = 0.75

minWidth = int(screen_width*coeffScreenSize)
minHeight = int(screen_height*coeffScreenSize)
# Configuración de la ventana
mainWindow.title(titleApp)
mainWindow.iconbitmap('img/app.ico')
mainWindow.geometry(str(minWidth) + "x" + str(minHeight))
mainWindow.config(bg=colorLightGreen)
mainWindow.minsize(minWidth, minHeight)
mainWindow.update()

# Widgets_Images
imgArduino = ImageTk.PhotoImage(Image.open('img/Arduino_Uno.png').resize((600,300)))

# Widgets_Frames
conectionFrame = tkinter.Frame(mainWindow)
conectionFrame.config(bg=colorLightGreen, width=minWidth, height=minHeight)
dataFrame = tkinter.Frame(mainWindow)
dataFrame.config(width=minWidth, height=minHeight)

# Widgets_Labels
labelTitle = tkinter.Label(conectionFrame)
labelTitle.config(text=titleApp, bg=colorLightGreen, font=(fontH1, sizeH1, "bold", "italic"), justify='center')
labelTitle.place(x=0.0,y=0.0,anchor='center')
labelImgArduino = tkinter.Label(conectionFrame, image=imgArduino, bg=colorLightGreen, justify='center')
labelImgArduino.place(x=0.0, y=0.0,anchor='center')
labelInfo = tkinter.Label(conectionFrame)
labelInfo.config(text="Conecte su Arduino Uno", bg=colorLightGreen, font=(fontH2,sizeH2), padx=10, justify='center')
labelInfo.place(x=0.0, y = 0.0, anchor='center')
labelCOMM = tkinter.Label(conectionFrame)
labelCOMM.config(text="COM:", bg=colorLightGreen, font=(fontH2,sizeH2), padx=10, justify='center')
labelCOMM.place(x=0.0, y = 0.0, anchor='center')

# Widgets_Entries
comNum = StringVar()

numberCOM = tkinter.Entry(conectionFrame, width=5, justify='center')
numberCOM.config(textvariable=comNum, validate="key",validatecommand=(mainWindow.register(on_changing_COM), '%P'), font=(fontH2,sizeH2))
numberCOM.place(x=0.0, y = 0.0, anchor='center')

# Widgets_Buttons
connectbutton = tkinter.Button(conectionFrame, text="Conectarse", command=on_connect, font=(fontH2,15))
connectbutton.place(x=0.0, y = 0.0, anchor='center')

# Pre-Loop
conectionFrame.pack(padx=25, pady=25)
dataFrame.pack(padx=250, pady=100)
mainWindow.update()
UpdatePlaces1()

#Events Handlers
mainWindow.protocol("WM_DELETE_WINDOW", on_closing)

# Bucle de la ventana
while(True):
    if(state == 1):
        UpdatePlaces1()
    mainWindow.update()
    if(closeArduino):
        break