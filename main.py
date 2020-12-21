#%%
from guizero import App, Text, Box, PushButton, Picture



import RPi.GPIO as GPIO
GPIO.setwarnings(False)        
GPIO.setmode(GPIO.BOARD)

app = App(title="My app", height=480, width=800, layout="grid")
app.tk.grid_columnconfigure((0,1,2,3,4),weight=1,minsize=50,)
app.tk.grid_rowconfigure((0,1,2),weight=1,minsize=100)

class button():
    
    def __init__(self,index,picture,grid,gpio,process='default',subprocess='default',state=0):
        
        self.index = index
        self.picture = picture
        self.grid = grid
        self.gpio = gpio
        self.process = process
        self.subprocess =subprocess

        
        
        
        


        
def do_nothing(a):
    return 0

def home_button():
    startScreen.visible=True
    buttonHome.visible=False
    lincolnScreen.visible=False
    KemppiScreen.visible=False
    return 0

def start_page(n):
    buttonHome.visible=True
    startScreen.visible=False
    print('Start Page selection()',n)
    if n == 0:
        lincolnScreen.visible=True        
    else:
        KemppiScreen.visible=True
    return 0

def process(n):
    print(n)
    
    return 0

    # def gpio_callback(n):
#     print('gpio_callback()',n)
#     if GPIO.input(buttons[n].gpio) == 1:
#         pushButtons[n].image = buttons[n].image+'_on.png'
#         GPIO.output(buttons[n].gpio,GPIO.LOW)
#     else:
#         pushButtons[n].image = buttons[n].image+'_off.png'
#         GPIO.output(buttons[n].gpio,GPIO.HIGH)

#Home button
buttonHome = PushButton(app, image="button_home.png",grid=[2,0],align="top", command= lambda: home_button(),visible=False)
buttonHome.tk.config(bd=0)

#select machine buttons
startScreen = Box(app,layout="grid", grid=[2,1])


startScreenButtons = []
# index,picture,grid,gpio
startScreenButtons.append(button(0,"lincoln",[0,0],0))
startScreenButtons.append(button(1,"button_blank",[1,0],0))
startScreenButtons.append(button(2,"kemppi"  ,[2,0],0))

startScreenButtonsPushButtons=[]
for buttons in startScreenButtons:
    startScreenButtonsPushButtons.append(PushButton(startScreen, args=[buttons.index], command=start_page, grid=buttons.grid, image =buttons.picture+'.png'))
    startScreenButtonsPushButtons[buttons.index].tk.config(bd=0)


#Kemppi select SUBprocess buttons 

KemppiScreen = Box(app,layout="grid", grid=[2,1],visible=False)
KemppiScreen.tk.grid_columnconfigure((0,1,2,3,4,5,6),weight=1,minsize=40)

kemppiScreenButtons = []
# index,picture,grid,gpio,process,subprocess
kemppiScreenButtons.append(button(0,"kemppiAC",[1,0],40,'tig','AC'))
kemppiScreenButtons.append(button(1,"kemppiDC",[3,0],38,'tig','DC'))
kemppiScreenButtons.append(button(2,"kemppiPulsed",[5,0],36,'tig','pulsed'))

kemppiScreenButtonsPushButtons=[]
for buttons in kemppiScreenButtons:
    kemppiScreenButtonsPushButtons.append(PushButton(KemppiScreen, args=[buttons.index], command=process, grid=buttons.grid, image =buttons.picture+'_OFF.png'))
    kemppiScreenButtonsPushButtons[buttons.index].tk.config(bd=0)

#lincoln select process buttons 

lincolnScreen = Box(app,layout="grid", grid=[2,1],visible=False)

lincolnScreen.tk.grid_columnconfigure((1,3,5,7),weight=1,minsize=100)
lincolnScreen.tk.grid_columnconfigure((0,2,4,6,8),weight=1,minsize=10)


lincolnScreenButtons = []
# index,picture,grid,gpio
lincolnScreenButtons.append(button(0,"lincolnPulsed",[1,0],37))
lincolnScreenButtons.append(button(1,"lincolnDIP",[3,0],35))
lincolnScreenButtons.append(button(2,"lincolnSpray",[5,0],33))
lincolnScreenButtons.append(button(3,"lincolnSTT",[7,0],32))

lincolnScreenButtonsPushButtons=[]
for buttons in lincolnScreenButtons:
    lincolnScreenButtonsPushButtons.append(PushButton(lincolnScreen, args=[buttons.index], command=start_page, grid=buttons.grid, image =buttons.picture+'_OFF.png'))
    lincolnScreenButtonsPushButtons[buttons.index].tk.config(bd=0)



app.display()