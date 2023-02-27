import js
p5 = js.window

x = 150
speed = 0.75
radius = 50
ySpeed = 0.25
y = 20

rect_x = 100
rect_y = 100
rect_w = 100
rect_h = 100

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)
    global x, speed, y, ySpeed
    x = x + speed
    y = y + ySpeed
    p5.noFill()
    d = dist(x, p5.mouseX,y, p5.mouseY)
    if (x > p5.width + radius) or (x < -radius):
        speed = -speed
    if (y > p5.height + radius) or (y < -radius):
        ySpeed = -ySpeed
    if (d < radius):
        p5.fill(200)
    else:
        p5.fill(255)
    p5.ellipse(x, y, radius*2, radius*2)
    p5.text("dist: "+ str(d), 10,50)
    p5.noFill()

    p5.rect(rect_x, rect_y, rect_w, rect_h)
    if ((p5.mouseX > rect_x) and (p5.mouseX < rect_x + rect_w)) and ((p5.mouseY > rect_y) and (p5.mouseY < rect_y + rect_h)):
        p5.fill(100)
        p5.text("XXX", 10,50)










        


def dist(x1, x2, y1, y2):
    dx = x2-x1
    dy = y2-y1
    distance = p5.sqrt(dx*dx + dy*dy)
    return distance


    





