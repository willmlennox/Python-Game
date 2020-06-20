from tkinter import *
from time import *
from math import *
from random import *

root = Tk()
screen = Canvas( root, width=1000, height=700, background = "white" )
screen.pack()

def imports():

    global GokuImage, GokuShootImage, SaibaSprite, background

    GokuImage = PhotoImage(file = "gokusprite2.gif")
    GokuShootImage = PhotoImage(file = "gokusprite1.gif")
    SaibaSprite = PhotoImage(file = "saibasprite1.gif")

    background = PhotoImage(file = "skybackground.gif")

def drawBackground():

    screen.create_image(400, 350,  image = background)

def checkHit():

    global saiba
    
    for i in range (len(kameBlasts)):

        for n in range (len(saiba)):

            if xBlast[i] + 5 > xsaiba[n] and yBlast[i] <= ysaiba[n] + 50 and yBlast[i] + 5 <= ysaiba[n] and xBlast[i] < xsaiba[n] + 25:
                screen.delete(kameBlasts[i])
                

def drawSaiba():

    global saibaspeedx, saiba, xsaiba, ysaiba, roundTime

    for n in range (saibasamount):

        saibaspeedx.append(-4)
        xsaiba.append(randint(1200, 1700))
        ysaiba.append(randint(25, 700))
        saiba.append(0)

        
    for i in range (saibasamount):
        screen.delete(saiba[i])
        xsaiba[i] = xsaiba[i] + saibaspeedx[i]
        saiba[i] = screen.create_image(xsaiba[i], ysaiba[i], image = SaibaSprite)

    screen.update()
    sleep(0.03)

def drawGoku():

    global Goku, shoot

    screen.delete(Goku)
    if shoot == True:
       
        Goku = screen.create_image(xGoku, yGoku,  image = GokuShootImage)

        if difference >= 0.50:
            
            shoot = False

    else:
        Goku = screen.create_image(xGoku, yGoku,  image = GokuImage)

def drawIntroScreen():
    global playButton

    playButton = Button(root, text = "CLICK TO PLAY", font = "Helvetica 40", command = playButtonPressed, anchor=CENTER)
    playButton.pack()
    playButton.place(x = 300, y = 450)

    screen.update()

def playButtonPressed():
    global gameMode, playButton

    playButton.destroy()
                         
    gameMode = "play"
    runGame()

    
def setInitialValues():

    global xSpeed, ySpeed, xGoku, yGoku, Goku, saibas, saibaspeedx, saibasamount, roundtime, saiba, xsaiba, ysaiba, saibaspeedx, roundTime
    global kameBlasts, blastSpeed, xBlast, yBlast, shoot
    global timeStart, timeFinish, difference, blastTime, blastDifference, blastTimeFinish

#Goku   
    xSpeed = 0
    ySpeed = 0
    xGoku = 50
    yGoku = 350

    Goku = screen.create_image(xGoku, yGoku,  image = GokuImage)
    
#Kame blasts
    kameBlasts = []
    xBlast = []
    yBlast = []
    blastSpeed = 20
#Saibamen values
    saibasamount = 10
    saibaspeedx = []
    saiba = []
    xsaiba = []
    ysaiba = []

    roundTime = 1000
    
    shoot = 0
    
#Time
    timeStart = 0
    timeFinish = 0
    difference = 0

    blastTime = 0
    blastTimeFinish = 0
    blastDifference = 0
    
def keyDownHandler( event ):

    global xSpeed, ySpeed

    if event.keysym == "Up":   #UP ARROW WAS PRESSED
        ySpeed = -10

    elif event.keysym == "Down":   #DOWN ARROW WAS PRESSED
        ySpeed = 10

    elif event.keysym == "x":
        spawnNewBlast()

def keyUpHandler( event ):
    global xSpeed, ySpeed

    xSpeed = 0
    ySpeed = 0

def spawnNewBlast():
    global kameBlasts, xBlast, yBlast, xGoku, yGoku, Goku, timeStart, shoot, blastTime
    if blastDifference >= 0.2:
        blastTime = time()
        timeStart = time()
        shoot = True
        xBlast.append( xGoku )
        yBlast.append( yGoku )
        kameBlasts.append(0)
        
    

def updateGokuPosition():
    global xGoku, yGoku
    
    xGoku = xGoku + xSpeed  #xSpeed will be zero unless the user is holding down an arrow key
    yGoku = yGoku + ySpeed

def checkGokuBoundaries():

    global yGoku

    if yGoku < 25:

        yGoku = yGoku + 5

    if yGoku > 675:

        yGoku = yGoku - 5

def updateBlastPositions():
    global kameBlasts, xBlast, yBlast

    for i in range(0,len(xBlast)):
        
        xBlast[i] = xBlast[i] + blastSpeed

        if xBlast[i] + 5 > xsaiba[i]:

            screen.delete(kameBlasts[i])

    deleteArrayItemsThatAreOffScreen()
            
#Deletes Ki Blasts that go off screen
def deleteArrayItemsThatAreOffScreen():
    
    i = 0
    
    while i < len(xBlast) - 1:
        if xBlast[i] > 1000:
            yBlast.pop(i)
            xBlast.pop(i)
            kameBlasts.pop(i)

        else:
            i = i + 1

#Draws Ki Blasts
def drawBlasts():
    
    for i in range(0,len(yBlast)):
        
        kameBlasts[i] = screen.create_oval(xBlast[i] - 5, yBlast[i] - 5,xBlast[i] + 5,yBlast[i] + 5,fill = "yellow", outline = "orange")

def deleteBlasts():
    
    for i in range(0,len(yBlast)):
        
       screen.delete(kameBlasts[i])

def start():
    global gameMode
    
    gameMode = "intro screen"  #"play" and "instructions" are the other possible values for this string
    drawIntroScreen()

#Start the game
def runGame():

    global timeFinish, difference, shoot, blastDifference
    imports()
    setInitialValues()
    drawBackground()

    #The animation loop.  Repeats once for every frame in the animation
    while True:
        updateGokuPosition()
        updateBlastPositions()
        drawGoku()
        drawBlasts()
        drawSaiba()
        #checkHit()
        checkGokuBoundaries()

        timeFinish = time()
        difference = timeFinish - timeStart

        blastTimeFinish = time()
        blastDifference = blastTimeFinish - blastTime

        screen.update()
        sleep(0.01)


        screen.delete(Goku)
        deleteBlasts()

    stopGame()


screen.bind( "<Key>", keyDownHandler)
screen.bind( "<KeyRelease>", keyUpHandler)

        

root.after(0, start)
screen.pack()
screen.focus_set()
root.mainloop()
