from engine.generalFunctions import *
from engine.being import Being


class Hero(Being):
    """
    player character
    """

    def __init__(self, location, coordinates, species):
        Being.__init__(self, location, coordinates, species)
        #log information about hero's birth
        log('msg', 'a hero is born')

    def chooseAction(self):
        """
        choose action basing on players input
        """
        from data.keyMapping import keyMapping_

        actionKey = getKeyInput()
        #wait for valid command
        while not isSet(keyMapping_, actionKey):
            log('warning', 'unknown action')
            actionKey = getKeyInput()
        #return corresponding method name
        return keyMapping_[actionKey]

    @doc_inherit
    def performAction(self, actionName, *actionParameters_):
        result = Being.performAction(self, actionName, *actionParameters_)
        #try to log corresponding message
        self.msg(actionName)
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
        #the world is a cold place now
        from engine.world import World
        World.gameOver = True
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
            #display stuff found at current tile
            self.location.getTileByCoordinates(self.coordinates).displayPresentItems()
            #in the end report success of movement
            return True

    @doc_inherit
    def addItems(self, *items_):
        #add items normally
        Being.addItems(self, *items_)
        #log information about quantity of added items
        log('msg', 'added ' + str(len(items_)) + ' item(s)')

    @doc_inherit
    def getItemsFrom(self, inventory=False):
        #if no outer inventory is provided, assume own inventory is needed
        if not inventory:
            inventory = self.inventory
        #get items normally
        items_ = Being.getItemsFrom(self, inventory)
        #if own inventory is considered
        if inventory == self.inventory:
            #log information about quantity of removed items
            log('msg', 'dropped ' + str(len(items_)) + ' item(s)')
        #return items in question
        return items_

    @doc_inherit
    def collect(self):
        #check if there is anything to take
        if self.getCurrentTile().accessInventory().isEmpty():
            #if not - send proper information
            log('msg', 'nothing to pick up here')
            return False
        #if tile is not empty, proceed normally
        Being.collect(self)

    @doc_inherit
    def drop(self):
        #check if there is anything to drop
        if self.inventory.isEmpty():
            #if not - send proper information
            log('msg', 'nothing to drop')
            return False
        #if tile is not empty, proceed normally
        Being.drop(self)

    def showInventory(self):
        """
        display owned items
        """
        if self.inventory.isEmpty():
            log('msg', 'inventory is empty')
        self.inventory.displayElements()