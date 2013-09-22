from generalFunctions import *
from view.view import *


class TileView(View):
    """
    display of tile
    """

    def displayItems(self):
        """
        display items present on this tile. if any
        """
        #if there are some items present on this tile
        if not self.model.hasEmptyInventory():
            self.model.getInventory().getView().callDisplayItems()