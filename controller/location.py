from utilities.generalFunctions import *
from controller.switch import *
from view.location import *


class LocationSwitch(Switch):
    """
    controller for location
    """

    def __init__(self, location):
        # call parent constructor
        Switch.__init__(self, location)
        # panel for displaying the world
        self.panel = LocationPanel(self)