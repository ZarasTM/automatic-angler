from ScreenScrapper import ScreenScrapper
import win32api, win32con, time

time.sleep(5)

# Object to get screen data
scr = ScreenScrapper()
scr.saveImg()

# State of a game
state = 0

def mainLoop():
    while true:
        scr.updateFrame()
