import js
p5 = js.window

gameScore = 0
highScore = 0
gameIsRunning = False

# class definition for the Point object:
class Player:  
    speed = 2
    color = 200
    def __init__(self, x = 0, y = 0):
        self.x = x  # initialize attribute x 
        self.y = y  # initialize attribute y 
    def draw(self):
        p5.fill(self.color)
        p5.push()
        p5.translate(self.x, self.y)
        p5.ellipse(0, 0, 20, 20)
        p5.pop()
    def move(self, x, y):
        self.x += x
        self.y += y
    def run(self):
        if (self.x > 298):
            self.x = 298
        if (self.x < 0):
            self.x = 2
        if (self.y < 0):
            self.y = 2
        if (self.y > 298):
            self.y = 298
        if (self.speed < 0):
            speed = 0.5
    def setColor(self, color):
        self.color = color
    def runTowardsObject(self, other_player):
        vectorX = other_player.x - self.x
        vectorY = other_player.y - self.y
        distance = ((vectorX ** 2) + (vectorY ** 2)) ** 0.5
        if distance > 0:
            vectorX /= distance
            vectorY /= distance
        self.move(vectorX * self.speed, vectorY * self.speed)
    def checkHit(self, other_player):
        global gameIsRunning
        if ((other_player.x > self.x - 15 and not other_player.x > self.x+15) and (other_player.y > self.y - 15 and not other_player.y > self.y+15)):
            gameIsRunning = False
        

class Slowie:
    def __init__(self, x = 0, y = 0):
        self.x = x  # initialize attribute x 
        self.y = y  # initialize attribute y 
    def draw(self):
        p5.fill(255,255,0)
        p5.push()
        p5.translate(self.x, self.y)
        p5.ellipse(0, 0, 20, 20)
        p5.pop()
    def run(self):
        global gameScore, highScore
        if ((player1.x > self.x - 20 and not player1.x > self.x+20) and (player1.y > self.y - 20 and not player1.y > self.y+20)):
            if (player2.speed > 0.5):
                player2.speed -= 0.1
            self.x = p5.random(300)
            self.y = p5.random(300)
            gameScore += 1
            if gameScore > highScore:
                highScore = gameScore

player1 = Player(0, 0)
player2 = Player(300,300)
player1.setColor(20)
player2.setColor(250)
player2.speed = 0.5
slowie1 = Slowie(150,150)
    
def setup():
    p5.createCanvas(300, 300)  
    
def draw():
    global gameScore, highScore
    if (gameIsRunning):
        p5.background(255)
        player1.draw()
        player1.run()
        player2.draw()
        player2.runTowardsObject(player1)
        player2.speed *= 1.001
        slowie1.draw()
        slowie1.run()
        player1.checkHit(player2)

        p5.fill(0)
        p5.text(gameScore, 10, 20)
        p5.text('HS: ' + str(highScore), 10, 40)

        if (p5.keyIsPressed == True):
            if (p5.keyCode == p5.LEFT_ARROW):
                player1.move(-player1.speed,0)
            elif (p5.keyCode == p5.RIGHT_ARROW):  # right arrow
                player1.move(player1.speed,0)
            elif (p5.keyCode == p5.UP_ARROW):  # up arrow
                player1.move(0,-player1.speed)
            elif (p5.keyCode == p5.DOWN_ARROW):  # down arrow
                player1.move(0,player1.speed)
    else:
        p5.fill(0,0,250)
        p5.text('Press enter to Restart.', 150-60, 150-10)
        p5.fill(0)

def keyPressed(event):
    global gameIsRunning, gameScore
    if (p5.keyCode == p5.ENTER):
        if (gameIsRunning == False):
            gameScore = 0
            gameIsRunning = True
            player1.x = 0
            player1.y = 0
            slowie1.x = 150
            slowie1.y = 150
            player2.x = 300
            player2.y = 300
            player2.speed = 0.5

def keyReleased(event):
    pass

def mousePressed(event):
    pass

def mouseReleased(event):
    pass