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
        #assign controller
        self.controller = TestItemView(self)


class TestItemView(ItemController):

    def display(self):
        print('some item #' + str(self.model.id))