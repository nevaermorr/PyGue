"""
environment for testing purposes
"""
#general classes
from engine.location import Location
from machine.hero import MetaHero
from data.item.testItem import TestItem

#tailored test data
from data.location.template.testLocation import grid_


def initEnvironment():
    #a single map will do for now
    locations_ = [Location(grid_)]
    #pointer to current location
    currentLocation = locations_[0]

    hero = MetaHero(currentLocation, [0, 0], 'goblin')
    stuff = TestItem(currentLocation, [2, 2])
    moreStuff = TestItem(currentLocation, [2, 2])

    for i in range(52):
        TestItem(currentLocation, [0, 1])

    return locations_