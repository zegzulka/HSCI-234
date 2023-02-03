import js
import random
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def spawnQuad(x, y, width, height):
    x1 = x
    x2 = x+width
    y1 = y
    y2 = y+height
    p5.fill(0)
    p5.quad(x1, y1, x2, y1, x2, y2, x1 ,y2)
    p5.noFill()

def quadRandomPosition(x, y, width, height):
    for j in range (0, 20):
        for i in range(0, 100):
            spawnQuad(random.randint(i*width, (1+i)*width), y*j, width, height)

def draw():
    p5.background(255)           # white background
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 20)
    quadRandomPosition(0,38, 20, 38)
