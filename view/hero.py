from generalFunctions import *
from view.being import *


class HeroView(BeingView):
    """
    display of hero
    """

    def __init__(self, model):
        View.__init__(self, model)

        #import key map
        from data.keyMap import hero_
        self.keyMap = hero_

        #notify about birth of Hero
        print('a Hero is born')

    def callActionWait(self):
        print('hero waits')

    def callActionQuit(self):
        print('nothing to do here...')

    def callActionChooseItems(self):
        print('hero have fallen during his quest')

    def callActionChooseItems(self):
        print('choose items to pick up')

    def callActionMove(self, actionResult):
        #for successful movement
        if actionResult:
            print('hero moved to', self.model.getCoordinates())
            #try to display items on newly stepped tile
            self.model.getCurrentTile().getView().displayItems()
        else:
            #this situation is managed by callActionCanMoveTo variant
            pass

    def callActionCanMoveTo(self, actionResult, destination):
        #if movement is not possible
        if not actionResult:
            #when there is no destination
            if not destination:
                print('unable to move there')
            #when destination exists, but is not accessible for some reason
            else:
                print('unable to move to', destination.getCoordinates())

    def callActionCollect(self, actionResult, collectedItems_=[]):
        #when nothing was collected due to lack of items possible to collect
        if not actionResult:
            print('nothing to pick up')
        #when attempt to collect some items was made
        else:
            #nothing seemed of interest
            if not collectedItems_:
                print('nothing was picked up')
            #some items were chosen to be collected
            else:
                print('picked up', len(collectedItems_), 'items')

    def callActionDrop(self, actionResult, droppedItems_=[]):
        #when nothing was dropped due to lack of items possible to drop
        if not actionResult:
            print('nothing to drop')
        #when attempt to dropped some items was made
        else:
            #no items were chosen to be dropped
            if not droppedItems_:
                print('nothing was dropped')
            #some items were chosen to be dropped
            else:
                print('dropped', len(droppedItems_), 'items')

    def callShowInventory(self):
        self.model.getInventory().getView().callDisplayItems()

    def chooseAction(self):
        """
        choose action basing on players input
        """

        actionKey = getKeyInput()
        #wait for valid command
        while not isSet(self.keyMap, actionKey):
            print('unknown action')
            actionKey = getKeyInput()
        #return corresponding method name
        return self.keyMap[actionKey]
