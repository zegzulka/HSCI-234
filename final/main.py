import js
p5 = js.window

#Game Manager
class GameManager():
    state = 'start'

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
    
    def objectChecker(self):
        pass

    #Main Action Function
    def buttonPressed(self, button):

        #A Action
        if(button == 'a'):
            body.rightFinger = 'a'
        
        #B Action
        elif(button == 'b'):
            body.rightFinger = 'b'

        #Left Action
        if(button == 'left'):
            body.leftFinger = 'left'

        #Right Action
        elif(button == 'right'):
            body.leftFinger = 'right'

        #Up Action
        elif(button == 'up'):
            body.leftFinger = 'up'

        #Down Action
        elif(button == 'down'):
            body.leftFinger = 'down'

        #Default State
        if(button == 'default'):
            body.rightFinger = 'default'
            body.leftFinger = 'default'

#Gameboy Image + Display
class Gameboy():
    colorChoice = 1
    def __init__(self):
        self.color = p5.loadImage('color.png'); 
        self.buttons = p5.loadImage('buttons.png');  
        self.leftDot = p5.loadImage('leftDot.png');  
        self.axisJoystick = p5.loadImage('axisJoystick.png');  
        self.display = p5.loadImage('display.png');  
        self.aroundBorder = p5.loadImage('aroundBorder.png');   
        self.displayBorder = p5.loadImage('displayBorder.png');  
        self.mainBorder = p5.loadImage('mainBorder.png');
    def draw(self):
        #Main Body Color
        if (self.colorChoice == 1):
            p5.background(35,185,0)
            p5.image(self.color, 0, 0) 
        if (self.colorChoice == 2):
            p5.background(35,185,0)
            p5.image(self.color, 0, 0) 
        
        #Project Display
        p5.image(self.display,0,0) #Display BG
        p5.push()
        p5.translate(105,59)
        self.Display.draw(self)
        p5.pop()

        #Around Border Color
        if (self.colorChoice == 1):
            p5.image(self.aroundBorder, 0, 0)   
        if (self.colorChoice == 2):
            p5.image(self.aroundBorder, 0, 0)

        #Body
        p5.image(self.buttons, 0, 0)  
        p5.image(self.leftDot, 0, 0)  
        p5.image(self.axisJoystick, 0, 0)  
        p5.image(self.displayBorder, 0, 0)  
        p5.image(self.mainBorder, 0, 0)

    #Display View
    class Display():
        def draw(self):
            if (gameManager.state == 'start'):
                p5.fill(250)
                p5.rect(0,0,20,20)

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

def setup():
    p5.createCanvas(300, 300)   

def draw():
    gameboy.draw()
    body.draw()
    controlsManager.keyChecker()
    

def keyPressed(event):
    pass

def keyReleased(event):
    controlsManager.buttonPressed('default')

def mousePressed(event):
    pass

def mouseReleased(event):
    controlsManager.buttonPressed('default')