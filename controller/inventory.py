from utilities.generalFunctions import *
from controller.switch import *


class InventorySwitch(Switch):
    """
    controller of inventory
    """

    def call_display_items(self):
        """
        display all items
        """

        # in case the inventory is empty
        if self.gear.is_empty():
            print('nothing here')

        # only if inventory have some items, display them
        else:
            # display each item separately
            for item in self.gear.get_items():
                item.get_switch().display()