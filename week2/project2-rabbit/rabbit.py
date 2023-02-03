import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def spawnRectangle(x, y, width, height, r, g, b):
    x1 = x
    x2 = x+width
    y1 = y
    y2 = y+height
    p5.strokeWeight(0)
    p5.fill(r, g, b)
    p5.quad(x1, y1, x2, y1, x2, y2, x1 ,y2)

def rectangleGrid(x, y, width, height, r, g, b):
    for j in range(0,20):
        for i in range(0, 30):
            spawnRectangle(width*-j + x + width*2*i, y + height*j, width, height, r, g, b)
    
def draw():
    p5.background(35,92,99)  
    rectangleGrid(0, 0, 20, 20, 97, 167, 176)
    p5.strokeWeight(2)
    p5.stroke(63,45,32)
    p5.fill(107,76,54)
    p5.ellipse(115, 190, 163)
    p5.fill(182,129,83)
    p5.quad(96,35,133,21,171,123,135,137)
    p5.fill(147,102,63)
    p5.quad(215,18,254,24,237,132,198,126)
    p5.fill(177,132,98)
    p5.ellipse(189, 171, 129)
    p5.fill(255,255,255)
    p5.ellipse(177, 155, 28)
    p5.fill(25,24,24)
    p5.ellipse(180, 158, 20)
    p5.fill(186,154,123)
    p5.ellipse(170, 261, 28)
    p5.fill(156,121,87)
    p5.ellipse(141, 261, 28)
    p5.fill(241,237,234)
    p5.ellipse(225, 199, 39)
    p5.fill(168,103,83)
    p5.ellipse(231, 204, 16)