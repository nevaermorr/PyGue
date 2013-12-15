from machine.item import *


class TestItem(MetaItem):
    """
    primitive item for testing purposes
    """
    __id = 1

    def __init__(self, location, coordinates_):
        Item.__init__(self, location, coordinates_)
        #assign unique id
        self.id = TestItem.__id
        TestItem.__id += 1

