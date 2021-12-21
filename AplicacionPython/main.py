import tkinter
import serial
import matplotlib.pyplot as Plot
from tkinter import StringVar, messagebox
from PIL import Image,ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Global variables
titleApp = "My Heart"
closeArduino = False
arduinoFind = False
colorBackground = "#abebc6"
portCOM = ""
fontH1 = 'Arabic Transparent'
sizeH1 = 40
fontH2 = 'Times New Roman'
sizeH2 = 20
sizeH3 = 14
state = 1
posXuserFrame = 25
arduino = None
nameUser = ""
surnameUser = ""
ageUser = ""
heightUser = ""
weightUSer = ""
spo2 = ""
bpm = ""
time = []
yEcg = []
yPuls = []

# Funciones
def on_closing():    
    if messagebox.askokcancel("Cerrar programa", "¿Estás seguro de que deseas cerrar esta ventana?"):
        global closeArduino
        closeArduino = True
        mainWindow.destroy()
        if(arduinoFind):
            arduino.close()
        print("SE CIERRA LA COMUNICACION")

def on_com(text):
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

def on_name(text):
    global nameUser
    if(not(str.isdigit(text)) or text==""):
        nameUser = text
        return True
    else:
        return False

def on_surname(text):
    global surnameUser
    if(not(str.isdigit(text)) or text==""):
        surnameUser = text
        return True
    else:
        return False

def on_age(text):
    global ageUser
    if(str.isdigit(text) or text==""):
        ageUser = text
        return True
    else:
        return False

def on_height(text):
    global heightUser
    if(str.isdigit(text) or text==""):
        heightUser = text
        return True
    else:
        return False

def on_weight(text):
    global weightUSer
    if(str.isdigit(text) or text==""):
        weightUSer = text
        return True
    else:
        return False

def on_connect():
    global arduino
    global arduinoFind
    global state
    try: 
        # Comunicación serie con el arduino
        arduino = serial.Serial(portCOM,9600)
    except serial.SerialException as e:
        labelInfo["text"] = "No se ha podigo conectar. Verifique si el puerto COM es el correcto."
        pass
    else:
        print("CONEXION CON ÉXITO")
        state = 2
        arduinoFind = True
        userFrame.pack(padx=200, pady=50)
        UpdateFrame2()
        conectionFrame.destroy()
        pass

def on_continue():
    global state, spo2, bpm
    state = 3
    labelNameFram3.config(text=nameUser+" "+surnameUser)
    spo2 = "-"
    bpm = "-"
    dataFrame.pack()
    UpdateFrame3()
    canvasEcg.get_tk_widget().pack()
    canvasPuls.get_tk_widget().pack()
    canvasEcg.get_tk_widget().config(width=ecgFrame.winfo_width(), height=ecgFrame.winfo_height())
    canvasPuls.get_tk_widget().config(width=pulsFrame.winfo_width(), height=pulsFrame.winfo_height())
    userFrame.destroy()

def UpdateFrame1():
    conectionFrame.config(width=mainWindow.winfo_width(),height=mainWindow.winfo_height())
    midWidth = conectionFrame.winfo_width()*0.5
    midtHeight = conectionFrame.winfo_height()*0.5
    labelImgArduino.place(x=midWidth, y=midtHeight-labelImgArduino.winfo_height()*0.25)
    labelTitle.place(x=midWidth, y=midtHeight-labelImgArduino.winfo_height()*0.75-labelTitle.winfo_height()*0.5-5)
    labelInfo.place(x=midWidth, y=midtHeight+labelImgArduino.winfo_height()*0.25+labelInfo.winfo_height()*0.5+5)
    heightCOMM = midtHeight+labelImgArduino.winfo_height()*0.25+labelInfo.winfo_height()+labelCOMM.winfo_height()*0.5+10
    labelCOMM.place(x=midWidth, y=heightCOMM)
    heightEntryCOMM = heightCOMM+labelCOMM.winfo_height()*0.5+numberCOM.winfo_height()*0.5+5
    numberCOM.place(x=midWidth, y=heightEntryCOMM)
    heightButtonConnect = heightEntryCOMM+numberCOM.winfo_height()*0.5+connectButton.winfo_height()*0.5 + 5
    connectButton.place(x=midWidth,y=heightButtonConnect)

def UpdateFrame2():
    labelImgUser.place(relx=0.9,rely=0.05,anchor='ne')
    labelName.place(x=posXuserFrame,y=posXuserFrame)
    newY = posXuserFrame + labelName.winfo_height() + 10
    nameEntry.place(x=posXuserFrame,y=newY)
    newY += nameEntry.winfo_height() + 10
    labelSurname.place(x=posXuserFrame,y=newY)
    newY += labelSurname.winfo_height() + 10
    surnameEntry.place(x=posXuserFrame,y=newY)
    newY += surnameEntry.winfo_height() + 10
    labelAge.place(x=posXuserFrame,y=newY)
    newY += labelAge.winfo_height() + 10
    ageEntry.place(x=posXuserFrame,y=newY)
    newY += ageEntry.winfo_height() + 10
    labelHeight.place(x=posXuserFrame,y=newY)
    newY += labelHeight.winfo_height() + 10
    heightEntry.place(x=posXuserFrame,y=newY)
    newY += heightEntry.winfo_height() + 10
    labelWeight.place(x=posXuserFrame,y=newY)
    newY += labelWeight.winfo_height() + 10
    weightEntry.place(x=posXuserFrame,y=newY)
    continueButton.place(relx=0.5,rely=0.95)

def UpdateFrame3():
    currentWidth = mainWindow.winfo_width()
    currentHeigth = mainWindow.winfo_height()
    dataFrame.config(width=currentWidth,height=currentHeigth)
    ecgFrame.config(width=currentWidth*0.7,height=currentHeigth*0.5)
    ecgFrame.place(x=0.0,y=0.0)
    pulsFrame.config(width=currentWidth*0.7,height=currentHeigth*0.5)
    pulsFrame.place(x=0.0,y=currentHeigth*0.5)
    parametersFrame.config(width=currentWidth*0.3,height=currentHeigth)
    parametersFrame.place(x=currentWidth-(currentWidth*0.3),y=0.0)
    labelNameFram3.place(relx=0.5,rely=0.3,anchor='center')
    labelSpo2.place(relx=0.2,rely=0.45)
    labelSpo2Value.place(relx=0.2,rely=0.5)
    labelSpo2Value.config(text=spo2)

# Ventana principal
mainWindow = tkinter.Tk()
mainWindow.resizable(False, False)

# Variables
screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()
coeffScreenSize = 0.7

minWidth = int(screen_width*coeffScreenSize)
minHeight = int(screen_height*coeffScreenSize)
print(str(minWidth) + " " + str(minHeight))

# Configuración de la ventana
mainWindow.title(titleApp)
mainWindow.iconbitmap('img/ecg2.ico')
mainWindow.geometry(str(minWidth) + "x" + str(minHeight))
mainWindow.config(bg=colorBackground)
mainWindow.minsize(minWidth, minHeight)
mainWindow.update()

# Widgets_Frames
conectionFrame = tkinter.Frame(mainWindow)
conectionFrame.config(bg=colorBackground, width=minWidth, height=minHeight)
userFrame = tkinter.Frame(mainWindow)
userFrame.config(width=minWidth, height=minHeight)
dataFrame = tkinter.Frame(mainWindow)
dataFrame.config(width=minWidth, height=minHeight)
ecgFrame = tkinter.Frame(dataFrame)
ecgFrame.config(width=minWidth*0.7, height=minHeight*0.5, bg=colorBackground)
ecgFrame.place(x=0.0,y=0.0)
pulsFrame = tkinter.Frame(dataFrame)
pulsFrame.config(width=minWidth*0.7, height=minHeight*0.5, bg=colorBackground)
pulsFrame.place(x=0.0,y=minHeight*0.5)
parametersFrame = tkinter.Frame(dataFrame)
parametersFrame.config(width=minWidth*0.3, height=minHeight, bg=colorBackground)
parametersFrame.place(x=minWidth-(minWidth*0.3),y=0.0)

# Widgets_Images
imgArduino = ImageTk.PhotoImage(Image.open('img/Arduino_Uno.png').resize((400,200)))
imgUser = ImageTk.PhotoImage(Image.open('img/User.png').resize((100,100)))

# Widgets_Labels
labelTitle = tkinter.Label(conectionFrame)
labelTitle.config(text=titleApp, bg=colorBackground, font=(fontH1, sizeH1, "bold", "italic"), justify='center')
labelTitle.place(x=0.0,y=0.0,anchor='center')
labelImgArduino = tkinter.Label(conectionFrame, image=imgArduino, bg=colorBackground, justify='center')
labelImgArduino.place(x=0.0, y=0.0,anchor='center')
labelInfo = tkinter.Label(conectionFrame)
labelInfo.config(text="Conecte su Arduino Uno", bg=colorBackground, font=(fontH2,sizeH2), justify='center')
labelInfo.place(x=0.0, y = 0.0, anchor='center')
labelCOMM = tkinter.Label(conectionFrame)
labelCOMM.config(text="COM:", bg=colorBackground, font=(fontH2,sizeH2), justify='center')
labelCOMM.place(x=0.0, y = 0.0, anchor='center')

labelImgUser = tkinter.Label(userFrame, bg="white", image=imgUser, justify='center')
labelImgUser.place(x=0.0, y=0.0,anchor='ne')
labelName = tkinter.Label(userFrame)
labelName.config(text="NOMBRE:", font=(fontH2,sizeH2), justify='center')
labelName.place(x=0.0,y=0.0)
labelSurname = tkinter.Label(userFrame)
labelSurname.config(text="APELLIDOS:", font=(fontH2,sizeH2), justify='center')
labelSurname.place(x=0.0,y=0.0)
labelAge = tkinter.Label(userFrame)
labelAge.config(text="EDAD:", font=(fontH2,sizeH2), justify='center')
labelAge.place(x=0.0,y=0.0)
labelHeight = tkinter.Label(userFrame)
labelHeight.config(text="ALTURA (cm):", font=(fontH2,sizeH2), justify='center')
labelHeight.place(x=0.0,y=0.0)
labelWeight = tkinter.Label(userFrame)
labelWeight.config(text="PESO (kg):", font=(fontH2,sizeH2), justify='center')
labelWeight.place(x=0.0,y=0.0)

labelNameFram3 = tkinter.Label(parametersFrame)
labelNameFram3.config(font=(fontH2,sizeH3), bg=colorBackground, justify='left')
labelNameFram3.place(x=0.0,y=0.0)
labelSpo2 = tkinter.Label(parametersFrame)
labelSpo2.config(text="SpO2:", bg=colorBackground, font=(fontH2, sizeH3), justify='left')
labelSpo2.place(x=0.0,y=0.0)
labelSpo2Value = tkinter.Label(parametersFrame)
labelSpo2Value.config(text=spo2, bg=colorBackground, font=(fontH2, sizeH3), justify='left')
labelSpo2Value.place(x=0.0,y=0.0)

# Widgets_Entries
comNum = StringVar()
name = StringVar()
surname = StringVar()
age = StringVar()
height = StringVar()
weigth = StringVar()
numberCOM = tkinter.Entry(conectionFrame, width=5, justify='center')
numberCOM.config(textvariable=comNum, validate="key",validatecommand=(mainWindow.register(on_com), '%P'), font=(fontH2,sizeH2))
numberCOM.place(x=0.0, y = 0.0, anchor='center')
nameEntry = tkinter.Entry(userFrame, font=(fontH2,sizeH3))
nameEntry.config(textvariable=name,validate="key",validatecommand=(mainWindow.register(on_name), '%P'),font=(fontH2,sizeH3))
nameEntry.place(x=0.0,y=0.0)
surnameEntry = tkinter.Entry(userFrame, font=(fontH2,sizeH3))
surnameEntry.config(textvariable=surname,validate="key",validatecommand=(mainWindow.register(on_surname), '%P'),font=(fontH2,sizeH3))
surnameEntry.place(x=0.0,y=0.0)
ageEntry = tkinter.Entry(userFrame, font=(fontH2,sizeH3))
ageEntry.config(textvariable=age,validate="key",validatecommand=(mainWindow.register(on_age), '%P'),font=(fontH2,sizeH3))
ageEntry.place(x=0.0,y=0.0)
heightEntry = tkinter.Entry(userFrame, font=(fontH2,sizeH3))
heightEntry.config(textvariable=height,validate="key",validatecommand=(mainWindow.register(on_height), '%P'),font=(fontH2,sizeH3))
heightEntry.place(x=0.0,y=0.0)
weightEntry = tkinter.Entry(userFrame, font=(fontH2,sizeH3))
weightEntry.config(textvariable=weigth,validate="key",validatecommand=(mainWindow.register(on_weight), '%P'),font=(fontH2,sizeH3))
weightEntry.place(x=0.0,y=0.0)

# Widgets_Buttons
connectButton = tkinter.Button(conectionFrame, text="Conectarse", command=on_connect, font=(fontH2,15))
connectButton.place(x=0.0, y = 0.0, anchor='center')
continueButton = tkinter.Button(userFrame, text="Continuar", command=on_continue, font=(fontH2,15), bg=colorBackground)
continueButton.place(x=0.0, y = 0.0, anchor='s')

# Graphs
figEcg, axEcg = Plot.subplots()
axEcg.set_title("Electrocardiograma")
axEcg.set_xlabel("Tiempo")
axEcg.set_ylabel("Actividad Eléctrica del Corazón")
axEcg.set_xlim(0,100)
axEcg.set_ylim(0, 5)
canvasEcg = FigureCanvasTkAgg(figEcg, ecgFrame)

figPuls, axPuls = Plot.subplots()
axPuls.set_title("Pulsioxímetro")
axPuls.set_xlabel("Tiempo")
axPuls.set_ylabel("Pulso")
axPuls.set_xlim(0,100)
axPuls.set_ylim(50, 150)
canvasPuls = FigureCanvasTkAgg(figPuls, pulsFrame)

# Pre-Loop
conectionFrame.pack(padx=25, pady=25)
mainWindow.update()
UpdateFrame1()
t = 0
timeMax = 100
#Events Handlers
mainWindow.protocol("WM_DELETE_WINDOW", on_closing)
# Bucle de la ventana
while(True):
    #if(state==3):
        #data = arduino.readline().decode('ascii').split(',')
        #print(data)
        #yEcg.append(float(data[0]))
        #time.append(t)
        #axEcg.plot(time, yEcg, 'r')
        #canvasEcg.draw()
        #canvasEcg.flush_events()
        #yPuls.append(float(data[1]))
        #axPuls.plot(time, yPuls, 'r')
        #canvasPuls.draw()
        #canvasPuls.flush_events()
        #labelSpo2Value.config(text=data[2])
        #if(len(yEcg)==100):
            #print("LEN IGUAL A 500")
            #timeMax += 100
            #yEcg = []
            #time = []
            #axEcg.clear()
            #axEcg.set_title("Electrocardiograma")
            #axEcg.set_xlabel("Tiempo")
            #axEcg.set_ylabel("Actividad Eléctrica del Corazón")
            #axEcg.set_xlim(timeMax-100,timeMax)
            #axEcg.set_ylim(0, 5)
            #yPuls = []
            #axPuls.clear()
            #axPuls.set_title("Pulsioxímetro")
            #axPuls.set_xlabel("Tiempo")
            #axPuls.set_ylabel("Pulso")
            #axPuls.set_xlim(timeMax-100,timeMax)
            #axPuls.set_ylim(50, 200)
        #t += 1
    if(closeArduino):
        break
    mainWindow.update()