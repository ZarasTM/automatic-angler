from PIL import Image, ImageGrab
import math
import logging
import logging.config

# Logger
logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
logger = logging.getLogger('screen_scrapper')

class ScreenScrapper:
    # Screen/Game resolution
    screenRes = [0, 0]
    gameRes = [0, 0]

    # Margin of game window
    margin = 0

    # Current game frame
    currFrame = []

    # Pixel data
    pullPix = [0, 0]    # Pixel to check if we got fish on hook
    resPix = [0, 0]     # Pixel to check if we should pull or release
    exitPix = [0, 0]    # Pixel to exit popup window

    # Constructor
    def __init__(self):
        self.screenRes = ImageGrab.grab().size
        self.calcGameWindow()
        logger.info("Initializing screen scrapper")
        self.updateFrame()

    # Calculates all data needed for operating with game itself
    def calcGameWindow(self):
        self.gameRes[0] = int((72*self.screenRes[1])/66)
        self.gameRes[1] = self.screenRes[1]
        self.margin = int((self.screenRes[0] - self.gameRes[0]) / 2)
        self.pullPix = [
            int(self.gameRes[0]/2),
            int(self.gameRes[1]*0.41)
        ]
        self.resPix = [
            int(self.gameRes[0]*0.438),
            int(self.gameRes[1]*0.4962)
        ]
        self.exitPix = [
            int(self.margin + self.gameRes[0]*0.904),
            int(self.gameRes[1]*0.207)
        ]
        logger.debug("Screen scrapper data:\n\tscreen_res=%s\n\tgame_res=%s\n\tmargin=%s\n\tpullPix=%s\n\tresPix=%s\n\texitPix=%s",
            self.screenRes,
            self.gameRes,
            self.margin,
            self.pullPix,
            self.resPix,
            self.exitPix
        )

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
