from generalFunctions import *
from engine.being import *
from view.hero import *


class Hero(Being):
    """
    player character
    """

    def __init__(self, location, coordinates_, species):
        #import key map
        from data.keyMap import hero_
        self.keyMap = hero_

        Being.__init__(self, location, coordinates_, species)
        #assign the view
        self.view = HeroView(self)

    def chooseAction(self):
        """
        choose action basing on players input
        """

        actionKey = getKeyInput()
        #wait for valid command
        while not isSet(self.keyMap, actionKey):
            self.log.warning('unknown action')
            actionKey = getKeyInput()
        #return corresponding method name
        return self.keyMap[actionKey]

    @doc_inherit
    def performAction(self, actionName, *actionParameters_):
        result = Being.performAction(self, actionName, *actionParameters_)
        #return original result
        return result

    @doc_inherit
    def loadSpeciesDependencies(self, species):
        Being.loadSpeciesDependencies(self, species)
        #only heroes can quit
        self.actionTimeCosts_['quit'] = 0

    def quit(self):
        """
        quit the game
        """
        #notify the world about pointlessness of its existence
        from engine.world import World
        World.gameOver = True
        #notify the view about the situation
        self.view.callActionQuit()
        #successful quit
        return True

    def die(self):
        """
        what happens when hero dies
        """
        Being.die(self)
        #leave it all behind
        self.quit()

    def move(self, direction):
        #move like other beings
        #if movement failed
        if not Being.move(self, direction):
            #report failure of movement
            return False
        #if movement succeeded
        else:
            #notify the view
            self.view.callActionMove(True)
            #report success of movement
            return True

    @doc_inherit
    def addItems(self, *items_):
        #add items normally
        Being.addItems(self, *items_)

    @doc_inherit
    def getItemsFrom(self, inventory=False):
        #if no outer inventory is provided, assume own inventory is needed
        if not inventory:
            inventory = self.inventory
        #get items normally
        items_ = Being.getItemsFrom(self, inventory)
        #return items in question
        return items_

    @doc_inherit
    def collect(self):
        #check if there is anything to take
        if self.getCurrentTile().accessInventory().isEmpty():
            return False
        #if tile is not empty, proceed normally
        return Being.collect(self)

    @doc_inherit
    def drop(self):
        #check if there is anything to drop
        if self.inventory.isEmpty():
            return False
        #if tile is not empty, proceed normally
        return Being.drop(self)

    def showInventory(self):
        """
        display owned items
        """
        if self.inventory.isEmpty():
            return False
        self.inventory.displayElements()
        return True