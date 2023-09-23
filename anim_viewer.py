from pico2d import *

open_canvas()

megaman = load_image('MEG1AMAN_A_Right_Transparent.bmp')

curFrame = 0
def attack_anim(frame):
    megaman.clip_draw(frame * 50, 860 - 50 * 3, 50, 50, 400, 100)
def run_anim(frame):
    megaman.clip_draw(frame * 50, 860 - 50 * 5, 50, 50, 400, 100)
def jump_anim(frame):
    if frame > 6:
        frame = 0
    megaman.clip_draw(frame * 50, 860 - 50 * 9, 50, 49, 400, 100)
def idle_anim(frame):
    megaman.clip_draw(frame * 50, 860 - 50 * 2, 50, 49, 400, 100)
megaman_state = 0
megaman_state_prev = 0
def input_handler():
    global megaman_state
    global curFrame
    events = get_events()
    for eve in events:
        if megaman_state != 0 and curFrame != 0 :
            break
        if eve.key == ord('a') or eve.key == ord('d'):
             megaman_state = 1
        elif eve.key == ord('w'):
             megaman_state = 3
        elif eve.key == 32:
             megaman_state = 2
    if curFrame == 0:
        megaman_state = 0
commands = {0:idle_anim,1:run_anim,2:attack_anim,3:jump_anim}
while True:
    input_handler()
    if megaman_state != megaman_state_prev:
        curFrame = 0
    commands[megaman_state](curFrame)
    update_canvas()
    clear_canvas()
    curFrame = (curFrame + 1) % 8
    megaman_state_prev = megaman_state
    delay(0.1)

