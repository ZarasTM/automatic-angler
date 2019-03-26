import pyautogui

class ScreenScrapper:
    # Screen resolution
    screenRes = [0, 0]

    # Game resolution
    gameRes = [0, 0]

    def __init__(self):
        self.screenRes = pyautogui.size()
        self.calcGameWindow()

    # Calculates all data needed for operating with game itself
    def calcGameWindow(self):
        self.gameRes[0] = self.screenRes[1]
        self.gameRes[1] = self.screenRes[1]
        print(self.gameRes)
