from controller.controller import *


class TileController(Controller):
    """
    display of tile
    """

    def displayItems(self):
        """
        display items present on this tile. if any
        """
        #if there are some items present on this tile
        if not self.model.hasEmptyInventory():
            self.model.getInventory().getController().callDisplayItems()