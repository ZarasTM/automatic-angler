from ScreenScrapper import ScreenScrapper
import pynput, time

'''
TODO:
    - Rewrite pixel color checking
    - Change pullCtrlPix coordinates
    - Add resPix
    - Start tests
'''


time.sleep(10)

keyCtrl = Controller()

# Object to get screen data
scr = ScreenScrapper()
scr.saveImg()

# State of a game
state = 0

def mainLoop():
    while true:
        scr.updateFrame()

        if state = 0:
            idleState()
        elif state = 1:
            prepState()
        elif state = 2:
            pullState()
        elif state = 3:
            restartState()
        else:
            print("Not recognized state number ", state)

# Idle state represented by 0
def idleState():
    time.sleep(1)
    keyCtrl.press(Key.space)
    state = 1

# Prep state represented by 1
def prepState():
    tmpPix = scr.currFrame[src.pullCtrlPix[0], src.pullCtrlPix[1]]

    if isInRange(tmpPix):
        state = 2

# Pull state represented by 2
def pullState():
    ctrlPix = scr.currFrame[src.pullCtrlPix[0], src.pullCtrlPix[1]]

    if isInRange(ctrlPix):
        keyCtrl.release(Key.space)
    else:
        keyCtrl.press(Key.space)

# Restart state represented by 2
def restartState():
    print("In restart state")

def isInRange(pix):
    if pix[0] > 57 && pix[0] < 65:
        if pix[1] > 95 && pix[1] < 103:
            if pix[2] > 131 && pix[2] < 139:
                return true
            else:
                return false
        else:
            return false
    else:
        return false
