from engine.generalFunctions import *
from engine.entity import Entity
from engine.inventory import *


class Being(Entity, InventoryInterface):
    """
    entity capable of taking actions
    """

    def __init__(self, location, coordinates, species):
        """
        create being
        :param location: location where the being is placed
        :param coordinates: coordinates depicting the position of being in given location
        :param species: species of this being
        """
        #inherited attributes from Entity
        Entity.__init__(self, location, coordinates)
        #provide the being with space for its belongings
        InventoryInterface.__init__(self)
        #load species-dependent features
        self.loadSpeciesDependencies(species)
        #announce that a new being has arrived
        location.checkIn(self)

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
            while not self.performAction(*self.chooseAction()):
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

    def chooseAction(self):
        """
        decide what to do
        """
        #pass by default
        return ['wait']

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
        pass

    def collect(self):
        """
        collect some items
        """
        #add items chosen from current tile's inventory
        self.addItems(*self.getItemsFrom(self.getCurrentTile().accessInventory()))