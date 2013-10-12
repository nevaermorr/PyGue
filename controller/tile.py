from utilities.generalFunctions import *
from controller.switch import *


class TileSwitch(Switch):
    """
    controller of tile
    """

    def display_items(self):
        """
        display items present on this tile. if any
        """
        # if there are some items present on this tile
        if not self.gear.has_empty_inventory():
            self.gear.get_inventory().get_switch().call_display_items()