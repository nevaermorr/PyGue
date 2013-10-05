from generalFunctions import *
from engine.entity import *
from engine.inventory import *
from view.being import *


class Being(Entity, InventoryInterface):
    """
    entity capable of taking actions
    """

    def __init__(self, location, coordinates_, species):
        """
        create being
        :param location: location where the being is placed
        :param coordinates_: coordinates depicting the position of being in given location
        :param species: species of this being
        """

        #inherited attributes from Entity
        Entity.__init__(self, location, coordinates_)
        #provide the being with space for its belongings
        InventoryInterface.__init__(self)
        #load species-dependent features
        self.loadSpeciesDependencies(species)
        #announce that a new being has arrived
        location.checkIn(self)
        #assign the view
        self.view = BeingView(self)

    def loadSpeciesDependencies(self, species):
        """
        load all species-dependent information
        :param species: species of this being
        """
        #remember species, just in case
        self.species = species
        #import proper file
        module = __import__('data.being.species.' + species, fromlist=[])
        speciesDependency = getattr(module.being.species, species)

        #time costs of different actions
        self.actionTimeCosts_ = speciesDependency.timeCosts_
        #time needed between creation and first action
        self.coolDown = speciesDependency.summoningSickness

    def act(self):
        """
        combination of all elements required to act
        """
        self.decreaseCoolDown()
        #if being is ready for action
        if self.isReadyToAct():
            #choose and try to perform some action until performed successfully
            while not self.performAction(*self.view.chooseAction()):
                pass

    def decreaseCoolDown(self):
        """
        decrease cool-down every time quantum
        """
        if self.coolDown > 0:
            self.coolDown -= 1

    def isReadyToAct(self):
        """
        check if the state of the being allows it to act
        """
        if self.coolDown == 0:
            return True

    def performAction(self, actionName, *actionParameters_):
        """
        call proper methods resolving certain actions
        :param actionName: name of desired action
        :param actionParameters_: list of parameters for action
        """
        #perform desired action
        actionResult = getattr(self, actionName)(*actionParameters_)
        #if action performed successfully
        if actionResult:
            #set cool-down to time cost of chosen action
            self.coolDown += self.actionTimeCosts_[actionName]
        #report success or failure of action
        return actionResult

    def react(self, action):
        """
        react to certain action
        :param action: list containing external action name and parameters
        """
        pass

    def die(self):
        """
        trigger all death effects
        """
        #this being is no more
        self.location.checkOut(self)

    def wait(self):
        """
        pass one turn
        """
        #wait is always successful
        return True

    def collect(self):
        """
        collect some items
        """
        #add items chosen from current tile's inventory
        collectedItems_ = self.getItemsFrom(self.getCurrentTile().getInventory())
        #if there is anything to pick up
        if collectedItems_:
            self.addItems(*collectedItems_)
            #notify view
            self.view.callActionCollect(True, collectedItems_)
            #collected successfully
            return True
        else:
            #failed to collect
            return False

    def drop(self):
        """
        drop some items
        """
        #choose items to drop (as for now - all)
        droppedItems = self.getItemsFrom()
        self.getCurrentTile().addItems(*droppedItems)
        #notify view
        self.view.callActionDrop(True, droppedItems)
        return True