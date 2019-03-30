from pynput import keyboard
import datetime
import logging

class KeyListener(keyboard.Listener):
    s, p, q = False, False, False

    def __init__(self, logger=None):
        super(KeyListener, self).__init__(self.on_press, self.on_release)
        self.logger = logger

    def on_press(self, key):
        keyStr = str(key)[1:-1]
        if keyStr == 's':
            self.logger.debug("%s: START", datetime.datetime.now())
            self.s = True
        elif keyStr == 'p':
            self.logger.debug("%s: PAUSE", datetime.datetime.now())
            self.p = not self.p
        elif keyStr == 'q':
            self.logger.debug("%s: QUIT", datetime.datetime.now())
            self.q = True


    def on_release(self, key):
        print()
