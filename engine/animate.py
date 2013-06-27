from engine.generalFunctions import *
from engine.entity import Entity


class Animate(Entity):
    """
    class corresponding to entities that can take actions
    """

    def __init__(self, location, coordinates):
        """
        creating animated entity
        :param location: location where the Entity is placed
        :param coordinates: coordinates depicting the position of Entity in given location
        """
        #inherited attributes
        Entity.__init__(self, location, coordinates)

        #cool-down time determines how much time quanta till entity can perform another act
        #entities get kind-of default "summoning sickness"
        self.coolDown = 100

    def act(self):
        """
        method combining all elements required to act
        """
        self.decreaseCoolDown()
        #if entity is ready for action
        if self.isReadyToAct():
            self.performAction(self.chooseAction())

    def decreaseCoolDown(self):
        """
        method decreasing cool-down every time quantum
        """
        if self.coolDown > 0:
            self.coolDown -= 1

    def isReadyToAct(self):
        """
        method checks if the state of the entity allows it to act
        """
        if self.coolDown == 0:
            return True

    def chooseAction(self):
        """
        method chooses action based on entity's choice
        """
        import sys

        actionKey = sys.stdin.read(1)
        if actionKey == '1':
            return ['move', ['NW']]
        if actionKey == '2':
            return ['move', ['N']]
        if actionKey == '3':
            return ['move', ['NE']]
        if actionKey == '4':
            return ['move', ['W']]
        if actionKey == '6':
            return ['move', ['E']]
        if actionKey == '7':
            return ['move', ['SW']]
        if actionKey == '8':
            return ['move', ['S']]
        if actionKey == '9':
            return ['move', ['SE']]
        #default action is a pass
        return None

    def performAction(self, action):
        """
        method calls proper methods resolving certain actions
        :param action: list containing desired action name and parameters
        """
        actionName = action[0]
        actionParameters = action[1]
        try:
            #for action 'foo' we try to automatically run method actionFoo()
            getattr(self, 'action' + actionName.capitalize())(*actionParameters)
        except AttributeError:
            #undefined action type
            return False

    def react(self, action):
        """
        method responsible for reaction to certain action
        :param action: list containing external action name and parameters
        """
        pass

    @doc_inherit
    def move(self, direction):
        Entity.move(self, direction)
        #if self.location.validateCoordinates(newCoordinates) == True: