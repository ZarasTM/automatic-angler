from pynput import keyboard, mouse
import datetime, sys, time, os
import logging, logging.config

# Check if log file is not too big
try:
    size = int(os.stat("./logs.log").st_size)

    # If file is larger than 10 MiB remove it
    if size > 10*1024*1024:
        os.remove("./logs.log")
except:
    pass

from ScreenScrapper import ScreenScrapper
from KeyListener import KeyListener

# Logger
logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
logger = logging.getLogger('root')

# Key and mouse clickers/listeners
logger.info("Initializing controllers")
keyCtrl = keyboard.Controller()
mouseCtrl = mouse.Controller()
listener = KeyListener()

logger.info("Starting listener")
listener.start()

# Wait until start
while not listener.s:
    if listener.q:
        break
    time.sleep(1)

# Object to get screen data
scr = ScreenScrapper()

# Controll pixel colors
pullColor = (73, 182, 53)
resColor = (225, 193, 50)

# State of a game
state = 0
logger.info("Entering main loop in idle state")

def mainLoop():
    while True:
        scr.updateFrame()

        # Handle quitting
        if listener.q:
            return False

        # Handle pausing
        if listener.p:
            keyCtrl.release(keyboard.Key.space)
            time.sleep(1)
            global state
            state = 0
            continue

        if state == 0:
            idleState()
        elif state == 1:
            prepState()
        elif state == 2:
            pullState()
        elif state == 3:
            restartState()
        else:
            logger.error("Not recognized state number %s", state)
            return False

# Idle state represented by 0
def idleState():
    time.sleep(1)
    keyCtrl.press(keyboard.Key.space)
    global state
    logger.info("Entering prep state")
    state = 1

# Prep state represented by 1
def prepState():
    tmpPix = scr.currFrame[scr.pullPix[0], scr.pullPix[1]]
    keyCtrl.press(keyboard.Key.space)

    if isInRange(tmpPix, pullColor, 4):
        global state
        logger.info("Entering pull state")
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
        logger.info("Entering restart state")
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
    logger.info("Entering idle state")
    state = 0

# Checks if given pixel color is in given color +- err
def isInRange(pix, col, err):
    logger.debug("Checking range for:\tPIX= %s\tCOL=%s\tERR=%s", pix, col, err)
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
