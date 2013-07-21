"""
environment for testing purposes
"""
#general classes
from engine.location import Location
from engine.hero import Hero
from engine.item import Item

#tailored test data
from data.location.template.testLocation import grid_


def initEnvironment():
    #a single map will do for now
    locations_ = [Location(grid_)]
    #pointer to current location
    currentLocation = locations_[0]

    hero = Hero(currentLocation, [0, 0], 'goblin')
    stuff = Item(currentLocation, [2, 2])
    moreStuff = Item(currentLocation, [2, 2])

    return locations_