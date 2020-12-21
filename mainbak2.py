#%%
from guizero import App, Text, Box, PushButton, Picture



import RPi.GPIO as GPIO
GPIO.setwarnings(False)        
GPIO.setmode(GPIO.BOARD)

weldingProcess = 'welding process'
WeldingSubProcess = 'sub process'

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
    mig.visible=False
    tig.visible=False
    return 0

def start_page(n):
    buttonHome.visible=True
    startScreen.visible=False
    print('Start Page selection()',n)
    if n == 0:
        mig.visible=True        
    else:
        tig.visible=True
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

# App 'papges'
startScreen = Box(app,layout="grid", grid=[2,1],visible=True)

tig = Box(app,layout="grid", grid=[2,1],visible=False)
#tig.tk.grid_columnconfigure((0,1,2,3,4,5,6),weight=1,minsize=40)

mig = Box(app,layout="grid", grid=[2,1],visible=False)
#mig.tk.grid_columnconfigure((1,3,5,7),weight=1,minsize=100)
#mig.tk.grid_columnconfigure((0,2,4,6,8),weight=1,minsize=10)


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
buttons.append(button(7,"lincolnDIP",[3,0],35,tig,'dip',0))
buttons.append(button(8,"lincolnSpray",[5,0],33,mig,'spray',0))
buttons.append(button(9,"lincolnSTT",[7,0],32,'mig','stt',0))

PushButtons=[]
for button in buttons:
    #if = kemppi add too kempi or else lincon
    PushButtons.append(PushButton(button.process, args=[button.index], command=start_page, grid=button.grid, image =button.picture+'_OFF.png'))
   ##                 (PushButton(startScreen, args=[buttons.index], command=start_page, grid=buttons.grid, image =buttons.picture+'.png'))
    #PushButton[button.index].tk.config(bd=0)
    # if button.process == 'tig' :
    #     tig[button.index].tk.config(bd=0)
    # elif button.process == 'mig' :
    #         mig[button.index].tk.config(bd=0)
    # else:
    #     start_page[button.index].tk.config(bd=0)
   




app.display()
# %%
