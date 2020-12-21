#%%

from guizero import App, Text, Box, PushButton, Picture

import RPi.GPIO as GPIO
GPIO.setwarnings(False)        
GPIO.setmode(GPIO.BOARD)

app = App(title="My app", height=480, width=800, layout="grid")
app.tk.grid_columnconfigure((0,1,2,3,4),weight=1,minsize=50,)
app.tk.grid_rowconfigure((0,1,2),weight=1,minsize=100)

class button():
    
    def __init__(self,index,picture,grid,gpio,process=None,subprocess=None,state=0):
        
        self.index = index
        self.picture = picture
        self.grid = grid
        self.gpio = gpio
        self.process = process
        self.subprocess =subprocess

class startButton():

    def __init__(self,picture,grid,gpio,process=None,subprocess=None,state=0):

        self.picture = picture
        self.grid = grid
        self.gpio = gpio
        self.process = process
        self.subprocess =subprocess




def home_button():
    startScreen.visible=True
    buttonHome.visible=False
    mig.visible=False
    tig.visible=False
    return 0

def do_nothing(a):
    print(a)

def subButtonPress(a):
    print(a)
    #

def buttonPress(a):
    startScreen.visible=False
    buttonHome.visible=True
    if buttons[a].picture == 'kemppi':
        print('button press =  kempi')
        tig.visible=True
        #buttons[a].process.visible=True
        #tig.visible=True
    elif buttons[a].picture == 'lincoln':
        print('button press =  lincoln')
        mig.visible=True

    else:
        do_nothing(buttons[a].subprocess)

# boxes
startScreen = Box(app,layout="grid", grid=[2,1],visible=True)

tig = Box(app,layout="grid", grid=[2,1],visible=False)
tig.tk.grid_columnconfigure((0,1,2,3,4,5,6),weight=1,minsize=40)

mig = Box(app,layout="grid", grid=[2,1],visible=False)
mig.tk.grid_columnconfigure((1,3,5,7),weight=1,minsize=100)
mig.tk.grid_columnconfigure((0,2,4,6,8),weight=1,minsize=10)


#app buttons
buttonHome = PushButton(app, image="button_home.png",grid=[2,0],align="top", command= lambda: home_button(),visible=True)
buttonHome.tk.config(bd=0)

startButton = startButton(picture='kempii',grid=[2,2],state=0,gpio=2)
PushButtonPushButton(app, args=[button.index], command=do_nothing, grid=button.grid, image = button.picture + '_OFF.png'))

# box buttons
buttons = []
# index,picture,grid,gpio,box type,subprocess
#index, picture, grid, gpio, process/page group, subprocess='default',state=0)

buttons.append(button(0,"lincoln",[0,0],0,startScreen,None,0))
buttons.append(button(1,"button_blank",[1,0],0,startScreen,None,0))
buttons.append(button(2,"kemppi"  ,[2,0],0,startScreen,None,0))
buttons.append(button(3,"kemppiAC",[1,0],40,tig,'AC',0))
buttons.append(button(4,"kemppiDC",[3,0],38,tig,'DC',0))
buttons.append(button(5,"kemppiPulsed",[5,0],36,tig,'pulsed',0))
buttons.append(button(6,"lincolnPulsed",[1,0],37,mig,'pulsed',0))
buttons.append(button(7,"lincolnDIP",[3,0],35,mig,'dip',0))
buttons.append(button(8,"lincolnSpray",[5,0],33,mig,'spray',0))
buttons.append(button(9,"lincolnSTT",[7,0],32,mig,'stt',0))

PushButtons=[]
for button in buttons:
    PushButtons.append(PushButton(button.process, args=[button.index], command=buttonPress, grid=button.grid, image = button.picture + '_OFF.png'))
    PushButtons[button.index].tk.config(bd=0)

for obj in buttons: 
    if obj.process == tig:
        print(str(obj.picture)) 

print(buttons[8].subprocess)





app.display()
