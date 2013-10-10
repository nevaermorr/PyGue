from utilities.generalFunctions import *
from controller.switch import *


class TileSwitch(Switch):
    """
    controller of tile
    """

    def displayItems(self):
        """
        display items present on this tile. if any
        """
        #if there are some items present on this tile
        if not self.gear.hasEmptyInventory():
            self.gear.getInventory().getSwitch().callDisplayItems()