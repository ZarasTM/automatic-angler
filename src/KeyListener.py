from pynput import keyboard
import logging, logging.config

# Logger
logging.config.fileConfig(fname='logging.conf', disable_existing_loggers=False)
logger = logging.getLogger('key_listener')

class KeyListener(keyboard.Listener):
    s, p, q, a = False, False, False

    def __init__(self):
        logger.info("Initializing key listener")
        super(KeyListener, self).__init__(self.on_press)

    def on_press(self, key):
        keyStr = str(key)[1:-1]
        if keyStr == 's':
            self.s = True
            logger.info("Starting bot")
        elif keyStr == 'p':
            self.p = not self.p
            logger.info("Pausing bot = %s", self.p)
        elif keyStr == 'q':
            self.q = True
            logger.info("Quitting bot")
		elif ketStr == 'a':
			self.a = True
			logger.info("Abandoning fish")
