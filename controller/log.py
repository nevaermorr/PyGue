from utilities.generalFunctions import *
from controller.switch import *


class LogSwitch(Switch):
    """
    controller of logged information
    """

    def callActionLog(self, info):
        """
        how to display information about undertaken actions
        """
        #for now just put it on the screen
        print(info)

    def callWarning(self, info):
        """
        how to display information about undertaken actions
        """
        #for now just put it on the screen
        print(info)

    def callError(self, info):
        """
        how to display information about undertaken actions
        """
        #for now just put it on the screen
        print(info)

    def callFatalError(self, info):
        """
        how to display information about undertaken actions
        """
        #for now just put it on the screen
        print(info)