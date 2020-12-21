#%%
from guizero import App, Text, Box, PushButton, Picture

app = App(title="My app", height=480, width=800, layout="grid")
app.tk.grid_columnconfigure((0,1,2,3,4),weight=1,)
app.tk.grid_rowconfigure((0,1,2),weight=1)

class button:
    def __init__(self,index,image,grid,gpio):
        self.index = index
        self.image = image
        self.grid = grid
        self.gpio = gpio
        

def gpio_callback(n):
    print('gpio_callback()',n)
    if GPIO.input(buttons[n].gpio) == 1:
        pushButtons[n].image = buttons[n].image+'_on.png'
        GPIO.output(buttons[n].gpio,GPIO.LOW)
    else:
        pushButtons[n].image = buttons[n].image+'_off.png'
        GPIO.output(buttons[n].gpio,GPIO.HIGH)
        
def do_nothing():
    return 0

def home_button():
    app.info("info", "this is a guizero app")
    startBox.visible=False

    return 0









#Home button
buttonHome = PushButton(app, image="button_home.png",grid=[2,0],align="top", command= lambda: home_button())
buttonHome.tk.config(bd=0)

#select mchine buttons
startScreen = Box(app,layout="grid", grid=[2,1])

buttonLincoln = PushButton(startScreen, image="lincoln.png", grid=[2,0])
buttonLincoln.tk.config(bd=0)

buttonBlank = PushButton(startScreen, image="button_blank.png",grid=[1,0])
buttonBlank.tk.config(bd=0)

buttonKemmpi = PushButton(startScreen, image="kemppi.png",grid=[0,0,])
buttonKemmpi.tk.config(bd=0)


startScreenButtons = []
# index,image,grid,gpio
startScreenButtons.append(button(0,'rear_lights' ,[0,0],40))
startScreenButtons.append(button(1,'front_lights',[1,0],38))
startScreenButtons.append(button(2,'water_pump'  ,[2,0],36))

startScreenButtonsPushButtons=[]
for button in buttons:
    GPIO.setup(button.gpio,GPIO.OUT)
    GPIO.output(button.gpio,GPIO.HIGH)
    pushButtons.append(PushButton(app, args=[button.index], command=general_callback, grid=button.grid, align='left', image = path + button.image+'_off.png'))





app.display()