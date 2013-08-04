from engine.generalFunctions import *


class DisplayableList:
    """
    a list with methods for printing and selecting items from screen
    """

    def __init__(self, list_):
        """
        initialization of displayable list
        :param list_: list to be displayed
        """
        #basis for this class - list of elements
        self.elements_ = list_

    def displayElements(self):
        """
        display elements of this list
        """
        #iteration counter
        i = 0
        for char in charGen():
            #check if the end of the list is reached
            if not isSet(self.elements_, i):
                break
            #display element
            print(char + ': ' + str(self.elements_[i]))
            #iterate counter
            i += 1