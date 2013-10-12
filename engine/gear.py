from engine.log import *


class Gear:
    """
    any element of the engine
    """
    # channel of communication common for whole engine
    log = Log()

    def __init__(self):
        self.switch = None

    def get_switch(self):
        """
        return switch of this gear
        """
        return self.switch