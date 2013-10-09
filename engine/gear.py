from engine.log import *


class Gear:
    """
    any element of the engine
    """
    #channel of communication common for whole engine
    log = Log()

    def __init__(self):
        self.controller = None

    def getController(self):
        """
        return controller of this gear
        """
        return self.controller