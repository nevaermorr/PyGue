from utilities.generalFunctions import *
from controller.switch import *
from controller.location import *
from view.world import WorldPanel


class WorldSwitch(Switch):
    """
    main controller for the game
    """

    def __init__(self, gear):
        """
        :param gear: world that will be managed
        """
        # call parent constructor
        Switch.__init__(self, gear)
        # panel for displaying the world
        self.panel = WorldPanel(self)

    def get_clock_switch(self):
        """
        access the controller of the clock
        """
        return self.gear.get_clock().get_switch()

    def call_set_current_location(self, location):
        """
        inform the switch about change of location
        """
        # assign switch of proper location
        self.panel.set_location_panel(location.get_switch().get_panel())

    def call_end_game(self):
        """
        inform the switch about end of the game
        """
        # print how much time have passed since the beginning
        print(self.gear.get_clock().get_time())