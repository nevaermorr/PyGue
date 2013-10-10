from utilities.generalFunctions import *
from controller.switch import *


class InventorySwitch(Switch):
    """
    controller of inventory
    """

    def callDisplayItems(self):
        """
        display all items
        """

        #in case the inventory is empty
        if self.gear.isEmpty():
            print('nothing here')

        #only if inventory have some items, display them
        else:
            #display each item separately
            for item in self.gear.getItems():
                item.getSwitch().display()