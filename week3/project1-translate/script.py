import js
p5 = js.window

def setup():
    p5.createCanvas(300, 300)    # 300 x 300 pixel canvas

savedPosition = []
scaleSave = 1

def drawChracter(x, y, scale):
    p5.push()
    p5.translate(x, y)
    p5.noStroke()
    p5.scale(scale);
    p5.fill(174,176,214)
    p5.rect(3, 0, 12, 1)
    p5.rect(3, 1, 1, 1)
    p5.rect(14, 1, 1, 1)
    p5.rect(4, 1, 0, 2)
    p5.rect(14, 2, 4, 1)
    p5.rect(0, 2, 4, 1)
    p5.rect(0, 3, 1, 16)
    p5.rect(17, 3, 1, 16)
    p5.rect(1, 18, 1, 1)
    p5.rect(16, 18, 1, 1)
    p5.rect(1, 19, 16, 1)
    p5.fill(108,70,46)
    p5.rect(4, 1, 10, 2)
    p5.rect(1, 3, 5, 2)
    p5.rect(12, 3, 5, 2)
    p5.rect(1, 5, 2, 12)
    p5.rect(15, 5, 2, 12)
    p5.rect(1, 17, 16, 1)
    p5.rect(2, 18, 14, 1)
    p5.fill(181,124,101)
    p5.rect(6, 3, 6, 2)
    p5.rect(6, 3, 6, 2)
    p5.rect(3, 5, 12, 12)
    p5.fill(108,70,46)
    p5.rect(5, 9, 3, 1)
    p5.rect(10, 9, 3, 1)
    p5.rect(8, 11, 2, 1)
    p5.rect(6, 14, 6, 1)
    p5.fill(255,229,219)
    p5.rect(7, 9, 1, 1)
    p5.rect(10, 9, 1, 1)
    p5.scale(1)
    p5.pop()
    
def draw():
    savedPosition.append([p5.mouseX-10*scaleSave, p5.mouseY-10*scaleSave, scaleSave])
    p5.background(10,30,86)

    for i in range(len(savedPosition)):
        drawChracter(savedPosition[i][0], savedPosition[i][1], savedPosition[i][2])
    if p5.mouseIsPressed:
        scaleSave = scaleSave + 0.1
    if scaleSave > 4:
        scaleSave = 1
    if len(savedPosition)>150:
        savedPosition.pop(0)