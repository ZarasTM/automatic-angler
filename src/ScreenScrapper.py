import PIL.ImageGrab

class ScreenScrapper:
    # Screen/Game resolution
    screenRes = [0, 0]
    gameRes = [0, 0]

    # Margin of game window
    margin = 0

    # Current game frame
    currFrame = []

    def __init__(self):
        self.screenRes = PIL.ImageGrab.grab().size
        self.calcGameWindow()
        self.updateFrame()

    # Calculates all data needed for operating with game itself
    def calcGameWindow(self):
        self.gameRes[0] = self.screenRes[1]
        self.gameRes[1] = self.screenRes[1]
        self.margin = (self.screenRes[0] - self.gameRes[0]) / 2

    # Updates game frame
    def updateFrame(self):
        self.currFrame = PIL.ImageGrab.grab(bbox=(
            self.margin,
            0,
            self.margin+self.gameRes[0],
            self.gameRes[1])).load()
