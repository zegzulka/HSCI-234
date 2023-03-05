import js
p5 = js.window

program_state = None
timer_start = 0
r = 0
g = 0
b = 0

def setup():
    global timer_start, program_state
    p5.createCanvas(300, 300)
    timer_start = p5.millis()
    program_state = 'state1'

def draw():
    global program_state, timer_start, r, g, b
    
    elapsed_time = p5.millis() - timer_start

    if elapsed_time > 10000:
        timer_start = p5.millis()
        program_state = 'state1'

    if elapsed_time > 5000 and program_state != 'state3':
        program_state = 'state2'

    p5.background(255)

    p5.fill(r, g, b)
    p5.rect(0, 0, 300, (elapsed_time / 1000) * 30)
    p5.fill(255)
    p5.text('timer: ' + str(int(elapsed_time/1000)), 10, 20)

    if program_state == 'state1':
        r, g, b = 250, 0, 250

    elif program_state == 'state2':
        r, g, b = 100, 250, 20

    elif program_state == 'state3':
        r, g, b = 0, 0, 0
        p5.fill(255)
        p5.ellipse(150,((elapsed_time / 1000) * 30)/2,((elapsed_time / 1000) * 30),((elapsed_time / 1000) * 30))

def keyPressed(event):
    pass

def keyReleased(event):
    pass

def mousePressed(event):
    global program_state
    program_state = 'state3'

def mouseReleased(event):
    global program_state
    program_state = 'state1'