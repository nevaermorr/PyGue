"""
environment for testing purposes
"""
# general classes
from machine.location import MetaLocation
from machine.hero import MetaHero
from data.item.test_item import TestItem

# tailored test data
from data.location.template.test_location import tiles_


def init_environment():
    # a single map will do for now
    locations_ = [MetaLocation(tiles_)]
    # pointer to current location
    current_location = locations_[0]

    hero = MetaHero(current_location, 0, 0, 'goblin')
    stuff = TestItem(current_location, 2, 2)
    more_stuff = TestItem(current_location, 2, 2)

    for i in range(52):
        TestItem(current_location, 0, 1)

    return locations_