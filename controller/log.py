from utilities.generalFunctions import *
from controller.switch import *


class LogSwitch(Switch):
    """
    controller of logged information
    """

    def call_action_log(self, info):
        """
        how to display information about undertaken actions
        """
        # for now just put it on the screen
        print(info)

    def call_warning(self, info):
        """
        how to display information about undertaken actions
        """
        # for now just put it on the screen
        print(info)

    def call_error(self, info):
        """
        how to display information about undertaken actions
        """
        # for now just put it on the screen
        print(info)

    def call_fatal_error(self, info):
        """
        how to display information about undertaken actions
        """
        # for now just put it on the screen
        print(info)