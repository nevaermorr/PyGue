from utilities.generalFunctions import *
from controller.switch import *


class WorldSwitch(Switch):
    """
    main controller for the game
    """

    def __init__(self, gear):
        #call parent constructor
        """
        :param gear: world that will be managed
        """
        Switch.__init__(self, gear)

    def call_end_game(self):
        """
        inform the switch about end of the game
        """
        print(self.gear.time.get_current_time())