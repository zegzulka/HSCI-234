import js
p5 = js.window

random_size1 = int(p5.random(25,125))
random_size2 = int(p5.random(25,125))
random_size3 = int(p5.random(25,125))
random_size4 = int(p5.random(25,125))
random_size5 = int(p5.random(25,50))

alpha = 0

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas 
    print('finished setup')

def draw():
    global alpha
    global random_size1, random_size2, random_size3, random_size4, random_size5
    p5.background(255)           # white background
    p5.text(str(p5.mouseX) + ", " + str(p5.mouseY), 10, 15)
    p5.strokeWeight(2)  # set stroke thickness
    p5.text(alpha, 10, 30)

    #rectangle changing transparency
    p5.stroke(127, 0, 255, alpha)
    random_square_at(0,0, random_size1)

    #rectangle changing color after hover
    p5.stroke(255, 127, 54)
    if (inside_square(300 - random_size2, 300 - random_size2, random_size2)):
        p5.stroke(255, 127, 54)
    else:
        p5.stroke(100, 50, 200)
    random_square_at(300 - random_size2,300 - random_size2, random_size2)

    #random rectangle
    p5.stroke(127, 200, 0)
    random_square_at(0,300 - random_size3, random_size3)

    #rectangle showing after clicking
    p5.stroke(255, 0, 127)
    if (p5.mouseIsPressed == True):
        random_square_at(300 - random_size4, 0, random_size4)
    
    if (alpha < 255):
        alpha = alpha + 1
    else:
        alpha = 0

    p5.stroke(0)
    random_square_loop(150,150, random_size5)


def random_square(size):
    p5.line(0,0, size, 0)
    p5.line(size, 0, size, size)
    p5.line(size, size, 0, size)
    p5.line(0,size, 0,0)

def random_square_at(x,y, size):
    p5.push()
    p5.translate(x,y)
    random_square(size)
    p5.pop()

def inside_square(posX, posY, random_size):
    if ((p5.mouseX > posX and p5.mouseX < posX + random_size) and (p5.mouseY > posY and p5.mouseY < posY + random_size)):
        p5.stroke(255, 127, 54)
        return True
    else:
        return False
    
#new moveto function for drawing lines - not working
def moveto(x1,y1):
    p5.push()
    p5.translate(x1,y1)

#new lineto function for drawing lines - not working
def lineto(x2,y2):
    p5.line(0,0,x2,y2)
    p5.pop()

def random_square_loop (x,y,size):
    for i in range (4):
        p5.stroke(p5.random(0,255), p5.random(0,255), p5.random(0,255))
        random_square_at(x-size*i/2,y-size*i/2,size*i)
        