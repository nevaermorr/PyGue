from utilities.generalFunctions import *
from controller.switch import *
from view.clock import *


class ClockSwitch(Switch):
    """
    controller for clock
    """

    def __init__(self, clock):
        # call parent constructor
        Switch.__init__(self, clock)
        # panel for displaying the world
        self.panel = ClockPanel(self)

    def get_time(self):
        """
        present the current time on the screen
        """
        return self.gear.get_time()