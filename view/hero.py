from generalFunctions import *
from view.being import *


class HeroView(BeingView):
    """
    display of hero
    """

    def __init__(self, model):
        View.__init__(self, model)
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
        else:
            #this situation is managed by callActionCanMoveTo variant
            pass

    def callActionCanMoveTo(self, actionResult, destination = False):
        if not actionResult:
            print('unable to move to',destination)