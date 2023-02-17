import js
p5 = js.window

angle = 0
x=150
y=150
circle_x=150
circle_y=150
circle_xspeed = 3
circle_yspeed = 2
circle_radius = 25
left_paddle_y = 150
right_paddle_y = 150

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 

def draw():
    p5.background(255)
    global angle
    global x, y
    global circle_x, circle_xspeed
    global circle_y, circle_yspeed
    p5.circle(circle_x, circle_y, 20);
    if (circle_x < circle_radius) or (circle_x > p5.width - circle_radius):
        circle_xspeed = -circle_xspeed
    if (circle_y < circle_radius) or (circle_y > p5.height - circle_radius):
        circle_yspeed = -circle_yspeed
    circle_x = circle_x + circle_xspeed
    circle_y = circle_y + circle_yspeed
    p5.ellipse(circle_x, circle_y, circle_radius*2, circle_radius*2)
    global left_paddle_y
    global right_paddle_y
    p5.rect(10, left_paddle_y, 20, 100)
    p5.rect(p5.width - 30, right_paddle_y, 20, 100)
    if (p5.keyIsPressed == True):
        if (p5.key == 'a'):
            left_paddle_y += 1
        else left_paddle_y += 0
        if (p5.key == 'y'):
            left_paddle_y -= 1
        else rigth_paddle_y += 0






