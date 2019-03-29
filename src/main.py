from ScreenScrapper import ScreenScrapper
from pynput import keyboard, mouse
import time

# Key and mouse clickers
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
            return False

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

    if isInRange(tmpPix, pullColor, 4):
        global state
        state = 2

# Pull state represented by 2
def pullState():
    catchPix = scr.currFrame[scr.pullPix[0], scr.pullPix[1]]
    stateChangePix = scr.currFrame[scr.resPix[0], scr.resPix[1]]

    # Pull controll
    if isInRange(catchPix, pullColor, 4):
        keyCtrl.release(keyboard.Key.space)
    else:
        keyCtrl.press(keyboard.Key.space)

    if isInRange(stateChangePix, resColor, 4):
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

# Checks if given pixel color is in given color +- err
def isInRange(pix, col, err):
    if pix[0] > col[0]-err and pix[0] < col[0]+err:
        if pix[1] > col[1]-err and pix[1] < col[1]+err:
            if pix[2] > col[2]-err and pix[2] < col[2]+err:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

mainLoop()
