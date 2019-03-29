from ScreenScrapper import ScreenScrapper
from pynput import keyboard, mouse
import time

keyCtrl = keyboard.Controller()
mouseCtrl = mouse.Controller()

# Give time to turn on game in full screen mode
time.sleep(5)

# Object to get screen data
scr = ScreenScrapper()

# Controll pixel colors
pullColor = (73, 182, 53)
resColor = (225, 193, 50)

# State of a game
state = 0

def mainLoop():
    while True:
        scr.updateFrame()

        if state == 0:
            idleState()
        elif state == 1:
            prepState()
        elif state == 2:
            pullState()
        elif state == 3:
            restartState()
        else:
            print("Not recognized state number ", state)

# Idle state represented by 0
def idleState():
    time.sleep(1)
    keyCtrl.press(keyboard.Key.space)
    global state
    state = 1

# Prep state represented by 1
def prepState():
    tmpPix = scr.currFrame[scr.pullPix[0], scr.pullPix[1]]
    keyCtrl.press(keyboard.Key.space)

    if isInRange(tmpPix, pullColor):
        global state
        state = 2

# Pull state represented by 2
def pullState():
    catchPix = scr.currFrame[scr.pullPix[0], scr.pullPix[1]]
    stateChangePix = scr.currFrame[scr.resPix[0], scr.resPix[1]]

    # Pull controll
    if isInRange(catchPix, pullColor):
        keyCtrl.release(keyboard.Key.space)
    else:
        keyCtrl.press(keyboard.Key.space)

    if isInRange(stateChangePix, resColor):
        global state
        state = 3

# Restart state represented by 3
def restartState():
    keyCtrl.release(keyboard.Key.space)

    # Click X in the corner of popup window
    mouseCtrl.position = scr.exitPix
    mouseCtrl.click(mouse.Button.left, 1)

    # Wait and reset focus on the game
    time.sleep(1)
    mouseCtrl.click(mouse.Button.left, 1)

    global state
    state = 0

def isInRange(pix, col):
    if pix[0] > col[0]-4 and pix[0] < col[0]+4:
        if pix[1] > col[1]-4 and pix[1] < col[1]+4:
            if pix[2] > col[2]-4 and pix[2] < col[2]+4:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

mainLoop()
