from pico2d import *

open_canvas()

backGround = load_image('TUK_GROUND.png')
megaman = load_image('MEG1AMAN_A_Right_Transparent.bmp')
TUK_WIDTH, TUK_HEIGHT = 1280, 1024

curFrame = 0
megaPos =[400,100]
def runRight_anim(frame):
    megaman.clip_composite_draw(frame * 50, 860 - 50 * 5, 50, 50,0,'',megaPos[0], megaPos[1],100,100)
def runLeft_anim(frame):
    megaman.clip_composite_draw(frame * 50, 860 - 50 * 5, 50, 50,0,'h',megaPos[0], megaPos[1],100,100)
def jumpRight_anim(frame):
    if frame > 6:
        frame = 0
    megaman.clip_composite_draw(frame * 50, 860 - 50 * 9, 50, 49,0,'', megaPos[0], megaPos[1],100,100)
def jumpLeft_anim(frame):
    if frame > 6:
        frame = 0
    megaman.clip_composite_draw(frame * 50, 860 - 50 * 9, 50, 49,0,'h', megaPos[0], megaPos[1],100,100)
def idleRight_anim(frame):
    megaman.clip_composite_draw(frame * 50, 860 - 50 * 2, 50, 49, 0, 'h', megaPos[0], megaPos[1], 100, 100)
def idleLeft_anim(frame):
    megaman.clip_composite_draw(frame * 50, 860 - 50 * 2, 50, 49,0,'', megaPos[0], megaPos[1],100,100)
def move_down(frame):
    megaman.clip_composite_draw(frame * 50, 0, 50, 80,0,'', megaPos[0], megaPos[1],100,100)
megaman_state = 0
megaman_state_prev = 0
def input_handler():
    global dx,dy
    global prevX,prevY
    global running
    events = get_events()
    for eve in events:
        if eve.type == SDL_KEYDOWN:
            if eve.key == SDLK_RIGHT:
                dx += 1
            elif eve.key == SDLK_LEFT:
                dx -= 1
            elif eve.key == SDLK_UP:
                dy += 1
            elif eve.key == SDLK_DOWN:
                dy -= 1
            elif eve.key == SDLK_ESCAPE:
                running = False
        elif eve.type == SDL_KEYUP:
            if eve.key == SDLK_RIGHT:
                prevX = dx
                dx -= 1
            elif eve.key == SDLK_LEFT:
                prevX = dx
                dx += 1
            elif eve.key == SDLK_UP:
                dy -= 1
            elif eve.key == SDLK_DOWN:
                dy += 1
def update_state():
    global  megaman_state
    if dy == 1:
        if prevX == 1:
            megaman_state = 4
        else :
            megaman_state = 5
    elif dy == -1:
        megaman_state = 6
    elif dx == 1:
        megaman_state = 3
    elif dx == -1:
        megaman_state = 2
    else:
        if prevX == 1:
            megaman_state = 0
        else:
            megaman_state = 1
def IsCollision(pos,size):
    if pos[0] >= 0 + size and pos[0] <= 800 - size and pos[1] >= 0 + size and pos[1] <=600 -size:
        return False
    return True
commands = {0:idleLeft_anim,1:idleRight_anim,2:runLeft_anim,3:runRight_anim,4:jumpRight_anim,5:jumpLeft_anim,6:move_down}
dx,dy=0,0
speed = 10
prevX,prevY = -1,-1
running = True
while True:
    input_handler()
    if not running:
        break
    update_state()
    megaPos[0] += dx * speed
    megaPos[1] += dy * speed
    if IsCollision(megaPos,50):
        megaPos[0] -= dx * speed
        megaPos[1] -= dy * speed
    backGround.composite_draw(0,'',400,300,800,600)
    commands[megaman_state](curFrame)

    update_canvas()
    clear_canvas()
    curFrame = (curFrame + 1) % 8
    delay(0.02)
close_canvas()
