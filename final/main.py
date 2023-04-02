import js
p5 = js.window

#Game Manager
class GameManager():
    state = 'start'
    buttonPressed = False
    lastButtonPressTime = 0
    played = False

    def draw(self):
        if (self.state == 'start'):
            start.draw()
        if (self.state == 'menu'):
            menu.draw()
        if (self.state == 'settings'):
            settings.draw()
        if (self.state == 'minecraft'):
            minecraft.draw()
        if (self.state == 'tetris'):
            tetris.draw()

    # Scene Actions
    def actionTriggered(self, button):
        currentTime = p5.millis()
        elapsed = currentTime - self.lastButtonPressTime

        # Start Scene
        if (self.state == 'start'):
            if elapsed >= 200:
                if (button == 'a'):
                    gameboy.clickSound.play()
                    self.state = 'menu'
                    self.lastButtonPressTime = currentTime
                    elapsed = 0

        # Menu Scene
        if (self.state == 'menu'):
            if elapsed >= 280:
                if button == 'up':
                    gameboy.clickSound.play()
                    if menu.triangleY == 36:
                        menu.triangleY = 70
                        menu.triangleX = 15
                    elif menu.triangleY == 46:
                        menu.triangleY = 36
                    elif menu.triangleY == 56:
                        menu.triangleY = 46
                    elif menu.triangleY == 70:
                        menu.triangleY = 56
                        menu.triangleX = 3

                if button == 'down':
                    gameboy.clickSound.play()
                    if menu.triangleY == 36:
                        menu.triangleY = 46
                    elif menu.triangleY == 46:
                        menu.triangleY = 56
                    elif menu.triangleY == 56:
                        menu.triangleY = 70
                        menu.triangleX = 15
                    elif menu.triangleY == 70:
                        menu.triangleY = 36
                        menu.triangleX = 3

                if button == 'b':
                    self.state = 'start'
                    gameboy.clickSound.play()

                if button == 'a':
                    gameboy.clickSound.play()
                    if menu.triangleY == 36:
                        self.savedChoice = gameboy.colorChoice
                        self.state = 'tetris'
                        gameboy.colorChoice = 4
                        elapsed = 0
                    elif menu.triangleY == 46:
                        self.savedChoice = gameboy.colorChoice
                        self.state = 'minecraft'
                        gameboy.colorChoice = 4
                        elapsed = 0
                    elif menu.triangleY == 56:
                        None
                    elif menu.triangleY == 70:
                        self.state = 'settings'
                        self.savedColor = gameboy.colorChoice
                        elapsed = 0
                self.lastButtonPressTime = currentTime

        #Minecraft Scene
        if (self.state == 'minecraft'):
            if elapsed >= 200:
                if (button == 'b'):
                    gameboy.clickSound.play()
                    self.state = 'menu'
                    gameboy.colorChoice = self.savedChoice
                if (button == 'a'):
                    None
                self.lastButtonPressTime = currentTime

        #Tetris Scene
        if (self.state == 'tetris'):
            if elapsed >= 200:
                if (button == 'b'):
                    gameboy.clickSound.play()
                    self.state = 'menu'
                    gameboy.colorChoice = self.savedChoice
                if (button == 'a'):
                    None
                self.lastButtonPressTime = currentTime
            
        
        #Settings Scene
        if (self.state == 'settings'):
            if elapsed >= 200:
                if button == 'up':
                    gameboy.clickSound.play()
                    if settings.triangleY == 36:
                        settings.triangleY = 56
                    elif settings.triangleY == 46:
                        settings.triangleY = 36
                    elif settings.triangleY == 56:
                        settings.triangleY = 46

                if button == 'down':
                    gameboy.clickSound.play()
                    if settings.triangleY == 36:
                        settings.triangleY = 46
                    elif settings.triangleY == 46:
                        settings.triangleY = 56
                    elif settings.triangleY == 56:
                        settings.triangleY = 36

                if button == 'b':
                    gameboy.clickSound.play()
                    self.state = 'menu'
                    gameboy.colorChoice = self.savedColor

                if button == 'a':
                    gameboy.clickSound.play()
                    if settings.triangleY == 36:
                        self.state = 'menu'
                        gameboy.colorChoice = 1
                    elif settings.triangleY == 46:
                        self.state = 'menu'
                        gameboy.colorChoice = 2
                    elif settings.triangleY == 56:
                        self.state = 'menu'
                        gameboy.colorChoice = 3

                self.lastButtonPressTime = currentTime

    def startupSoundPlay(self):
        currentTime = p5.millis()
        if ((currentTime > 2000) and (self.played == False)):
            gameboy.startupSound.play()
            self.played = True

              

#Start Scene Objects
class Start():
    def draw(self):
        p5.fill(10)
        p5.strokeWeight(0)
        p5.rect(-1, -1, 100, 91)
        p5.fill(250)
        p5.textSize(8)
        p5.textWrap(p5.WORD)
        p5.textAlign(p5.CENTER)
        p5.text('Welcome in the game!', 3, 20, 85)
        p5.textSize(7)
        p5.fill(150)
        p5.text('Press "A" to start.', 3, 60, 85)

#Menu Scene Objects
class Menu():
    triangleY = 36
    triangleX = 3

    def draw(self):
        p5.fill(10)
        p5.strokeWeight(0)
        p5.rect(-1, -1, 100, 91)

        p5.fill(250)
        p5.textSize(8)
        p5.textWrap(p5.WORD)
        p5.textAlign(p5.CENTER)
        p5.text('Choose a game:', 3, 18, 85)

        p5.triangle(self.triangleX, self.triangleY, self.triangleX+5, self.triangleY+3, self.triangleX, self.triangleY+6)
        p5.textSize(6)
        p5.fill(200)
        p5.text('Tetris', 3, 43, 85)

        p5.textSize(6)
        p5.fill(200)
        p5.text('Minecraft', 3, 53, 85)

        p5.textSize(6)
        p5.fill(200)
        p5.text('Pokemon', 3, 63, 85)

        p5.textSize(4)
        p5.fill(180)
        p5.text('Settings', 3, 75, 85)

#Settings Scene Objects
class Settings():
    triangleY = 36
    triangleX = 3

    def draw(self):
        p5.fill(10)
        p5.strokeWeight(0)
        p5.rect(-1, -1, 100, 91)

        p5.fill(250)
        p5.textSize(8)
        p5.textWrap(p5.WORD)
        p5.textAlign(p5.CENTER)
        p5.text('Change color:', 3, 18, 85)

        p5.triangle(self.triangleX, self.triangleY, self.triangleX+5,
                    self.triangleY+3, self.triangleX, self.triangleY+6)
        p5.textSize(6)
        p5.fill(200)
        p5.text('Blue', 3, 43, 85)

        p5.textSize(6)
        p5.fill(200)
        p5.text('Green', 3, 53, 85)

        p5.textSize(6)
        p5.fill(200)
        p5.text('Red', 3, 63, 85)

        if self.triangleY == 36:
            gameboy.colorChoice = 1
        elif self.triangleY == 46:
            gameboy.colorChoice = 2
        elif self.triangleY == 56:
            gameboy.colorChoice = 3

#Rectangle Scene Objects
class Rectangle():
    rectangleX = 20
    rectangleY = 20

    def draw(self):
        p5.fill(99, 99, 5)
        p5.strokeWeight(0)
        p5.rect(-1, -1, 100, 91)

        p5.strokeWeight(0)
        p5.stroke(133, 143, 7)
        p5.fill(230, 228, 0)
        p5.rect(self.rectangleX, self.rectangleY, 20, 20)

#Minecraft Scene Objects
class Minecraft():
    def __init__(self):
        self.video = p5.createVideo(['minecraft.mp4'])
        self.video.size(93, 85)
        self.video.hide()
        self.video.loop()
        self.video.volume(0)
        
    def draw(self):
        p5.fill(99, 99, 5)
        p5.strokeWeight(0)
        p5.rect(-1, -1, 100, 91)
        p5.image(gameboy.minecraftImage, 0,0,93,85)
        p5.image(self.video, 0, 0, 93, 85)

#Tetris Scene Objects
class Tetris():
    def __init__(self):
        self.tetrisVideo = p5.createVideo(['tetris.mp4'])
        self.tetrisVideo.size(93, 85)
        self.tetrisVideo.hide()
        self.tetrisVideo.loop()
        self.tetrisVideo.volume(0)

    def draw(self):
        p5.fill(99, 99, 5)
        p5.strokeWeight(0)
        p5.rect(-1, -1, 100, 91)
        p5.image(gameboy.minecraftImage, 0, 0, 93, 85)
        p5.image(self.tetrisVideo, 0, 0, 93, 85)

#Controls & Actions
class ControlsManager():
    def keyChecker(self):
        if(p5.keyIsPressed == True):
            if (p5.key == 'a') or (p5.key == 'A'):  
                self.buttonPressed('a')
            elif (p5.key == 'b') or (p5.key == 'B'):
                self.buttonPressed('b')
            elif (p5.keyCode == p5.LEFT_ARROW):
                self.buttonPressed('left')
            elif (p5.keyCode == p5.RIGHT_ARROW):
                self.buttonPressed('right')
            elif (p5.keyCode == p5.UP_ARROW):
                self.buttonPressed('up')
            elif (p5.keyCode == p5.DOWN_ARROW):
                self.buttonPressed('down')
        if(p5.mouseIsPressed == True):
            if ((p5.mouseX > 196 and p5.mouseX < 215) and (p5.mouseY > 176 and p5.mouseY < 195)):
                self.buttonPressed('a')
            elif ((p5.mouseX > 180-2 and p5.mouseX < 180+15+2) and (p5.mouseY > 194-2 and p5.mouseY < 194+15+2)):
                self.buttonPressed('b')
            if ((p5.mouseX > 88-2 and p5.mouseX < 88+15+2) and (p5.mouseY > 192-2 and p5.mouseY < 192+15+2)):
                self.buttonPressed('left')
            elif ((p5.mouseX > 108-2 and p5.mouseX < 108+15+2) and (p5.mouseY > 192-2 and p5.mouseY < 192+15+2)):
                self.buttonPressed('right')
            elif ((p5.mouseX > 98-2 and p5.mouseX < 98+15+2) and (p5.mouseY > 180-2 and p5.mouseY < 180+15+2)):
                self.buttonPressed('up')
            elif ((p5.mouseX > 98-2 and p5.mouseX < 98+15+2) and (p5.mouseY > 204-2 and p5.mouseY < 204+15+2)):
                self.buttonPressed('down')
            

    
    def objectChecker(self):
        pass

    #Main Action Function
    def buttonPressed(self, button):

        #A Action
        if(button == 'a'):
            body.rightFinger = 'a'
            gameManager.actionTriggered('a')
        
        #B Action
        elif(button == 'b'):
            body.rightFinger = 'b'
            gameManager.actionTriggered('b')

        #Left Action
        if(button == 'left'):
            body.leftFinger = 'left'
            gameManager.actionTriggered('left')

        #Right Action
        elif(button == 'right'):
            body.leftFinger = 'right'
            gameManager.actionTriggered('right')

        #Up Action
        elif(button == 'up'):
            body.leftFinger = 'up'
            gameManager.actionTriggered('up')

        #Down Action
        elif(button == 'down'):
            body.leftFinger = 'down'
            gameManager.actionTriggered('down')

        #Default State
        if(button == 'default'):
            body.rightFinger = 'default'
            body.leftFinger = 'default'
            gameManager.actionTriggered('default')

#Gameboy Image + Display
class Gameboy():
    colorChoice = 1
    def __init__(self):
        self.color1 = p5.loadImage('color1.png'); 
        self.color2 = p5.loadImage('color2.png');
        self.background2 = p5.loadImage('background2.png');
        self.buttons = p5.loadImage('buttons.png');  
        self.leftDot = p5.loadImage('leftDot.png');  
        self.axisJoystick = p5.loadImage('axisJoystick.png');  
        self.display = p5.loadImage('display.png');  
        self.aroundBorder = p5.loadImage('aroundBorder.png');   
        self.displayBorder = p5.loadImage('displayBorder.png');  
        self.mainBorder = p5.loadImage('mainBorder.png');
        self.font1 = p5.loadFont('PressStart2P.otf')
        self.clickSound = p5.loadSound('click.wav')
        self.startupSound = p5.loadSound('startup.wav')
        self.minecraftImage = p5.loadImage('minecraftImage.png')

    def draw(self):
        #Use font1 for all texts
        p5.textFont(self.font1);

        #Main Body Color
        if (self.colorChoice == 1):
            p5.background(0,127,172)
            p5.image(self.color1, 0, 0) 
        if (self.colorChoice == 2):
            p5.image(self.background2, 0, 0)
            p5.image(self.color2, 72, 21) 
        if (self.colorChoice == 3):
            p5.image(self.background2, 0, 0)
            p5.image(self.color2, 72, 21)
        if (self.colorChoice == 4):
            p5.image(self.background2, 0, 0)
            p5.image(self.color2, 72, 21)
        if (self.colorChoice == 5):
            p5.image(self.background2, 0, 0)
            p5.image(self.color2, 72, 21)
        if (self.colorChoice == 6):
            p5.image(self.background2, 0, 0)
            p5.image(self.color2, 72, 21)
        
        #Scene Display
        p5.image(self.display,0,0) #Display BG
        p5.push()
        p5.translate(106,59)
        gameManager.draw()
        p5.pop()

        #Around Border Color
        if (self.colorChoice == 1):
            p5.image(self.aroundBorder, 0, 0)   
        elif (self.colorChoice == 2):
            p5.image(self.aroundBorder, 0, 0)
        elif (self.colorChoice == 3):
            p5.image(self.aroundBorder, 0, 0)
        elif (self.colorChoice == 4):
            p5.image(self.aroundBorder, 0, 0)
        elif (self.colorChoice == 5):
            p5.image(self.aroundBorder, 0, 0)
        elif (self.colorChoice == 6):
            p5.image(self.aroundBorder, 0, 0)

        #Body
        p5.image(self.buttons, 0, 0)  
        p5.image(self.leftDot, 0, 0)  
        p5.image(self.axisJoystick, 0, 0)  
        p5.image(self.displayBorder, 0, 0)  
        p5.image(self.mainBorder, 0, 0)

#Fingers & Body
class Body():
    leftFinger = 'default'
    rightFinger = 'default'
    def __init__(self):
        self.rightHand = p5.loadImage('rightHand.png');  
        self.leftHand = p5.loadImage('leftHand.png');  
        self.fingerLeftLeft = p5.loadImage('fingerLeftLeft.png');  
        self.fingerLeftDefault = p5.loadImage('fingerLeftDefault.png');  
        self.fingerLeftUp = p5.loadImage('fingerLeftUp.png');  
        self.fingerLeftDown = p5.loadImage('fingerLeftDown.png');  
        self.fingerLeftRight = p5.loadImage('fingerLeftRight.png');  
        self.fingerRightDefault = p5.loadImage('fingerRightDefault.png');  
        self.fingerRightA = p5.loadImage('fingerRightA.png'); 
        self.fingerRightB = p5.loadImage('fingerRightB.png'); 
    def draw(self):
        #Body
        p5.image(self.rightHand, 0, 0)  
        p5.image(self.leftHand, 0, 0)  

        #Left Finger
        if (self.leftFinger == 'default'):
            p5.image(self.fingerLeftDefault, 0, 0)  
        if (self.leftFinger == 'left'):
            p5.image(self.fingerLeftLeft, 0, 0) 
        if (self.leftFinger == 'right'):
            p5.image(self.fingerLeftRight, 0, 0) 
        if (self.leftFinger == 'up'):
            p5.image(self.fingerLeftUp, 0, 0) 
        if (self.leftFinger == 'down'):
            p5.image(self.fingerLeftDown, 0, 0) 

        #Right Finger
        if (self.rightFinger == 'default'):
            p5.image(self.fingerRightDefault, 0, 0)  
        if (self.rightFinger == 'a'):
            p5.image(self.fingerRightA, 0, 0) 
        if (self.rightFinger == 'b'):
            p5.image(self.fingerRightB, 0, 0) 
        
gameboy = Gameboy()
body = Body()
controlsManager = ControlsManager()
gameManager = GameManager()
menu = Menu()
start = Start()
settings = Settings()
minecraft = Minecraft()
tetris = Tetris()

def setup():
    p5.createCanvas(300, 300)

def draw():
    gameboy.draw()
    body.draw()
    controlsManager.keyChecker()
    gameManager.startupSoundPlay()
    
    

def keyPressed(event):
    pass

def keyReleased(event):
    controlsManager.buttonPressed('default')

def mousePressed(event):
    pass

def mouseReleased(event):
    controlsManager.buttonPressed('default')
