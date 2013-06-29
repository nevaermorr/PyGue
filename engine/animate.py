from engine.generalFunctions import *
from engine.entity import Entity


class Animate(Entity):
    """
    class corresponding to entities that can take actions
    """

    def __init__(self, location, coordinates):
        """
        create animated entity
        :param location: location where the Entity is placed
        :param coordinates: coordinates depicting the position of Entity in given location
        """
        #inherited attributes
        Entity.__init__(self, location, coordinates)
        #give a signal to location, that some new animate entity arrived
        location.checkIn(self)

        #cool-down time determines how much time quanta till entity can perform another act
        #entities get kind-of default "summoning sickness"
        self.coolDown = 100

    def act(self):
        """
        combination of all elements required to act
        """
        self.decreaseCoolDown()
        #if entity is ready for action
        if self.isReadyToAct():
            self.performAction(self.chooseAction())
            pass

    def decreaseCoolDown(self):
        """
        decrease cool-down every time quantum
        """
        if self.coolDown > 0:
            self.coolDown -= 1

    def isReadyToAct(self):
        """
        check if the state of the entity allows it to act
        """
        if self.coolDown == 0:
            return True

    def chooseAction(self):
        """
        decide what to do
        """
        #pass by default
        return None

    def performAction(self, action):
        """
        call proper methods resolving certain actions
        :param action: list containing desired action name and parameters
        """
        #if none action selected, animated entity waits
        if action is None:
            return False

        actionName = action[0]
        actionParameters = action[1:]
        try:
            #for action 'foo' we try to automatically run method actionFoo()
            getattr(self, actionName)(*actionParameters)
        except AttributeError:
            #undefined action type
            print(actionName, ': no such action defined')
            return False

    def react(self, action):
        """
        method responsible for reaction to certain action
        :param action: list containing external action name and parameters
        """
        pass

    def die(self):
        """
        trigger all death effects
        """
        #this animate entity is no more
        self.location.checkOut()