from PIL import Image, ImageGrab
import math

class ScreenScrapper:
    # Screen/Game resolution
    screenRes = [0, 0]
    gameRes = [0, 0]

    # Margin of game window
    margin = 0

    # Current game frame
    currFrame = []

    # Pixel data
    pullCtrlPix = [0, 0]
    resPix = [0, 0]

    # Constructor
    def __init__(self):
        self.screenRes = ImageGrab.grab().size
        self.calcGameWindow()
        self.updateFrame()

    # Calculates all data needed for operating with game itself
    def calcGameWindow(self):
        self.gameRes[0] = int((72*self.screenRes[1])/66)
        self.gameRes[1] = self.screenRes[1]
        self.margin = int((self.screenRes[0] - self.gameRes[0]) / 2)
        self.pullCtrlPix = [
            int(self.gameRes[0]/2),
            int(self.gameRes[1]*0.422)
        ]

    # Updates game frame
    def updateFrame(self):
        self.currFrame = ImageGrab.grab(bbox=(
            self.margin,
            0,
            self.margin+self.gameRes[0],
            self.gameRes[1])
        ).load()

    # Saves image to a tmp.png file (mainly for developement)
    def saveImg(self):
        pix = []
        for col in range(self.gameRes[1]):
            for row in range(self.gameRes[0]):
                pix.append(self.currFrame[row, col])
        im = Image.new("RGB", (self.gameRes[0], self.gameRes[1]))
        im.putdata(pix)
        im.save("tmp.png")
