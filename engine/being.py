from engine.generalFunctions import *
from engine.entity import Entity


class Being(Entity):
    """
    entity capable of taking actions
    """

    def __init__(self, location, coordinates, type):
        """
        create being
        :param location: location where the being is placed
        :param coordinates: coordinates depicting the position of being in given location
        :param type: type of being
        """
        #inherited attributes
        Entity.__init__(self, location, coordinates)
        #load type-dependent features
        self.loadTypeDependencies(type)
        #give a signal to location, that some new being arrived
        location.checkIn(self)

        #cool-down time determines how much time quanta till being can perform another act
        #beings get kind-of "summoning sickness"
        self.coolDown = self.summoningSickness

    def loadTypeDependencies(self, type):
        """
        load all type-dependent information
        :param type: type of being
        """
        #remember type, just in case
        self.type = type
        #import proper file
        module = __import__('data.beingTypes.' + type, fromlist=[])
        typeDependency = getattr(module.beingTypes, type)

        #time costs of different actions
        self.actionTimeCosts_ = typeDependency.timeCosts_
        #time needed between creation and first action
        self.summoningSickness = typeDependency.summoningSickness

    def act(self):
        """
        combination of all elements required to act
        """
        self.decreaseCoolDown()
        #if being is ready for action
        if self.isReadyToAct():
            self.performAction(self.chooseAction())

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

    def performAction(self, action):
        """
        call proper methods resolving certain actions
        :param action: list containing desired action name and parameters
        """

        actionName = action[0]
        actionParameters = action[1:]
        try:
            #perform desired action and receive its time cost
            getattr(self, actionName)(*actionParameters)
            timeCost = self.actionTimeCosts_[actionName]
            #set cool-down time
            self.coolDown += timeCost
        except AttributeError:
            #undefined action type
            log('error', actionName, ': no such action defined')
            return False

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
        self.location.checkOut()

    def wait(self):
        """
        pass one turn
        """
        log('msg', 'entity waits')

    def move(self, direction):
        Entity.move(self, direction)
