from generalFunctions import *
from engine.item import *


class TestItem(Item):
    """
    primitive item for testing purposes
    """
    __id = 1

    def __init__(self, location, coordinates_):
        Item.__init__(self, location, coordinates_)
        #assign unique id
        self.id = TestItem.__id
        TestItem.__id += 1
        #assign view
        self.view = TestItemView(self)


from view.item import *


class TestItemView(ItemView):

    def display(self):
        print('some item #' + str(self.model.id))