import js
p5 = js.window

x = 150
speed = 0.75
radius = 50
ySpeed = 0.25
y = 20

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)
    global x, speed, y, ySpeed
    x = x + speed
    y = y + ySpeed
    if (x > p5.width + radius) or (x < -radius):
        speed = -speed
    if (y > p5.height + radius) or (y < -radius):
        ySpeed = -ySpeed
    p5.ellipse(x, y, radius*2, radius*2)