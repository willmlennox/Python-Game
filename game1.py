from tkinter import *
from time import *
from math import *
from random import *

root = Tk()
screen = Canvas( root, width=1000, height=700, background = "white" )
screen.pack()

#Importing images
def imports():

    global GokuImage, GokuShootImage, GokuDeathImage1, GokuDeathImage2, SaibaSprite, background, introScreen, playButtonImage, playAgainButton, quitGameButton

    GokuImage = PhotoImage(file = "gokusprite2.gif")
    GokuShootImage = PhotoImage(file = "gokusprite1.gif")
    GokuDeathImage1 = PhotoImage(file = "gokusprite3.gif")
    GokuDeathImage2 = PhotoImage(file = "gokusprite4.gif")
    SaibaSprite = PhotoImage(file = "saibasprite1.gif")
    introScreen = PhotoImage(file = "introbackground.gif")
    background = PhotoImage(file = "skybackground.gif")
    playButtonImage = PhotoImage(file = "playbuttonimage.gif")
    playAgainButton = PhotoImage(file = "playagainbutton.gif")
    quitGameButton = PhotoImage(file = "quitgamebutton.gif")

#Draws the background
def drawBackground():

    screen.create_image(400, 350,  image = background)

#Function to determine if a Saiba is hit
def hitBox():

    global xsaiba, ysaiba, xBlast, yBlast, kameBlasts, score, scoreDown, upSpeed, downSpeed

    if(len(xBlast)) != 0:

        for i in range(len(xsaiba)):

            x = 0
            while x < len(xBlast):
                
                c = sqrt((xsaiba[i] - xBlast[x]) ** 2 + (ysaiba[i] - yBlast[x]) ** 2)

                if c <= 30:
                    
                    upSpeed = upSpeed * 1.001
                    downSpeed = downSpeed * 1.001
                    xsaiba[i] = randint(1050, 1150)
                    ysaiba[i] = randint(25, 700)

                    screen.delete(kameBlasts[x])
                    yBlast.remove(yBlast[x])
                    xBlast.remove(xBlast[x])
                    kameBlasts.remove(kameBlasts[x])

                    scoreDown = False
                    drawScore()

                else:
                    
                    x = x + 1

#Creates and updates health
def healthDown():

    global hp, health
    
    health = health - 40
    screen.delete(hp)
    hp = screen.create_rectangle(10, 10, 10 + health, 20, fill = "red")
    screen.update()

#Creates starting health
def drawHealth():

    global hp

    screen.delete(hp)
    hp = screen.create_rectangle(10, 10, 10 + health, 20, fill = "red")
    screen.update()

#Draws score and calls to healthDown function when enemy gets past and if health is 0
def drawScore():

    global score, showscore, health

    if scoreDown == True:

        healthDown()

    else:
    
        score = score + 10

    screen.delete(showscore)
    showscore = screen.create_text(900, 50, text = (score), font = 150, fill = "white")
    screen.update()
    
    if health == 0:

        endGame()

#Resets the Saiba when they go off screen
def offScreenSaiba():

    global scoreDown
    
    for i in range(len(xsaiba)):

        if xsaiba[i] <= - 10:

            xsaiba[i] = randint(1050, 1150)
            ysaiba[i] = randint(25, 700)
            scoreDown = True
            drawScore()
            
#Creates the Saiba and moves them
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
    
#Draws Goku's shooting and basic images
def drawGoku():

    global Goku, shoot

    screen.delete(Goku)
    
    if shoot == True:
        
        screen.delete(Goku)
        Goku = screen.create_image(xGoku, yGoku,  image = GokuShootImage)
        screen.update()
        

        if difference >= 0.50:
            
            shoot = False

    else:
        
        screen.delete(Goku)
        Goku = screen.create_image(xGoku, yGoku,  image = GokuImage)
        screen.update()

#Creates the intro screen
def drawIntroScreen():

    imports()

    screen.create_image(500,350, image = introScreen)
    screen.create_image(515, 575, image = playButtonImage)
    root.bind("<Button-1>", introScreenClick)


#Detects clicks for intro screen
def introScreenClick(event):
    
    xMouse = event.x
    yMouse = event.y

    if 370 <= xMouse <= 650 and 525 <= yMouse <= 625:
        
        runGame()

#Does animation for end game and cancels runGame
def endGame():
    global score, ySpeed, game, Goku

    screen.delete(Goku)
    Goku = screen.create_image(xGoku, yGoku,  image = GokuDeathImage1)
    screen.update()
    sleep(1)

    screen.delete(Goku)
    Goku = screen.create_image(xGoku, yGoku,  image = GokuDeathImage2)
    screen.update()
    
    game = 0
    
    #End game message
    endMessage = screen.create_text( 500,350, text = "YOU LOST!", font = "Helvetica 48 bold", fill = "white" )
    screen.update()
    sleep(1.25)
    screen.delete(endMessage)

        
    #Displays score and play again/quit buttons
    screen.create_text(500,100, text = "Final Score:", font = "Helvetica 18", fill = "white" )
    screen.create_text(500,150, text = score, font = "Helvetica 64 bold", fill = "white" )
    screen.create_image(200, 625, image = playAgainButton)
    screen.create_image(800, 625, image = quitGameButton)

    root.bind("<Button-1>", endGameClick)


#Detects clicks for end game screen
def endGameClick(event):
    
    xMouse = event.x
    yMouse = event.y

    if 50 <= xMouse <= 350 and 550 <= yMouse <= 700:
        
        runGame()
        
    elif 650 <= xMouse <= 950 and 550 <= yMouse <= 700:
        
        root.destroy()

#Sets initial values
def setInitialValues():

    global xSpeed, ySpeed, xGoku, yGoku, Goku, saibas, saibaspeedx, saibasamount, roundtime, saiba, xsaiba, ysaiba, saibaspeedx, upSpeed, downSpeed
    global kameBlasts, blastSpeed, xBlast, yBlast, shoot
    global timeStart, timeFinish, difference, blastTime, blastDifference, blastTimeFinish, hitbox, score, showscore, scoreDown, game, health, hp

    game = 1

#Goku   
    xSpeed = 0
    ySpeed = 0
    xGoku = 50
    yGoku = 350
    upSpeed = -12
    downSpeed = 12
    Goku = screen.create_image(xGoku, yGoku,  image = GokuImage)
    
#Kame blasts
    kameBlasts = []
    xBlast = []
    yBlast = []
    blastSpeed = 30
    
#Saibamen values
    saibasamount = 10
    saibaspeedx = []
    saiba = []
    xsaiba = []
    ysaiba = []

#Score values
    score = 0
    showscore = 0
    scoreDown = False
    
    shoot = 0

#Health values
    health = 200
    hp = 0
    
#Time
    timeStart = 0
    timeFinish = 0
    difference = 0

    blastTime = 0
    blastTimeFinish = 0
    blastDifference = 0

#Binds movement keys and others
def keyDownHandler( event ):

    global xSpeed, ySpeed, upSpeed, downSpeed

    if event.keysym == "Up":
        
        ySpeed = upSpeed

    elif event.keysym == "Down":
        
        ySpeed = downSpeed

    elif event.keysym == "x":
        
        spawnNewBlast()

    elif event.keysym == "q":
        
        endGame()

#Stops the movements of character when buttons aren't pressed
def keyUpHandler( event ):
    
    global xSpeed, ySpeed

    xSpeed = 0
    ySpeed = 0

#Appends values to each Ki Blast and adds a delay between each
def spawnNewBlast():
    
    global kameBlasts, xBlast, yBlast, xGoku, yGoku, Goku, timeStart, shoot, blastTime
    
    if blastDifference >= 0.2:
        
        blastTime = time()
        timeStart = time()
        
        shoot = True
        
        xBlast.append( xGoku )
        yBlast.append( yGoku )
        kameBlasts.append(0)
        
#Moves Goku
def updateGokuPosition():
    global xGoku, yGoku
    
    xGoku = xGoku + xSpeed
    yGoku = yGoku + ySpeed

#Makes sure Goku can't go off screen
def checkGokuBoundaries():

    global yGoku

    if yGoku < 25:

        yGoku = yGoku + 5

    if yGoku > 675:

        yGoku = yGoku - 5

#Moves Ki Blasts
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

#Creates Ki Blasts
def drawBlasts():
    
    for i in range(0,len(yBlast)):
        
        kameBlasts[i] = screen.create_oval(xBlast[i] - 5, yBlast[i] - 5,xBlast[i] + 5,yBlast[i] + 5,fill = "yellow", outline = "orange")

#Deletes Ki Blasts individually
def deleteBlasts():
    
    for i in range(0,len(yBlast)):
        
       screen.delete(kameBlasts[i])

#Starts with intro screen instead of going right into the game
def start():
    
    global gameMode
    
    gameMode = "intro screen"
    drawIntroScreen()

#Starts the game
def runGame():

    global timeFinish, difference, shoot, blastDifference
    imports()
    setInitialValues()
    drawBackground()

    #The animation loop.  Repeats once for every frame in the animation
    while game == 1:
        updateGokuPosition()
        updateBlastPositions()
        drawHealth()
        drawGoku()
        drawBlasts()
        drawSaiba()
        hitBox()
        offScreenSaiba()
        checkGokuBoundaries()

        timeFinish = time()
        difference = timeFinish - timeStart

        blastTimeFinish = time()
        blastDifference = blastTimeFinish - blastTime

        screen.update()
        sleep(0.03)

        deleteBlasts()

screen.bind( "<Key>", keyDownHandler)
screen.bind( "<KeyRelease>", keyUpHandler)

root.after(0, drawIntroScreen)
screen.pack()
screen.focus_set()
root.mainloop()
