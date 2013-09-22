from generalFunctions import *
from view.view import *


class InventoryView(View):
    """
    display of inventory
    """

    def callDisplayItems(self):
        """
        display all items
        """

        #in case the inventory is empty
        if self.model.isEmpty():
            print('nothing here')

        #only if inventory have some items, display them
        else:
            #display each item separately
            for item in self.model.getItems():
                item.getView().display()