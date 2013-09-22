from generalFunctions import *
from engine.log import *
from view.view import *


class Gear:
    """
    any element of the engine
    """
    #channel of communication common for whole engine
    log = Log()

    def getView(self):
        """
        return view of this gear
        """
        try:
            return self.view
        except AttributeError:
            return None