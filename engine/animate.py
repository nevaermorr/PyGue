from engine.generalFunctions import *
class Animate:
    "class corresponding to entities that can take actions"
    
    def __init__(self):
        "creating animated entity"
        #cool-down time determines how much time quanta till entity can perform another act
        self.coolDown = 0
    
    def act(self):
        self.decreaseCoolDown()
        #if entity is ready for action
        if self.isReadyToAct():
            self.performAction(self.chooseAction())
    
    def decreaseCoolDown(self):
        "method decreasing cool-down every time quantum"
        if self.coolDown > 0:
            self.coolDown -= 1
            
    def isReadyToAct(self):
        "method checks if the state of the entity allows it to act"
        if self.coolDown == 0:
            return True
    
    def chooseAction(self):
        "method chooses action based on entity's choice"
        #default action is a pass
        return None
    
    def performAction(self, action):
        "method calls proper methods resolving certain actions"
        x = action
        try:
            #for action 'foo' we try to automatically run method actionFoo()
            getattr(self, 'action'+action.capitalize())
        except AttributeError:
            return False
    
    def react(self):
        pass
    
    def move(self):
        pass
        #if self.location.validateCoordinates(newCoordinates) == True: