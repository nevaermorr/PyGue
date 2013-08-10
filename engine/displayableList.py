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
        #import key map
        from data.keyMap import displayableList_
        self.keyMap = displayableList_
        #basis for this class - list of elements
        self.elements_ = list_

    def displayElements(self):
        """
        display elements of this list (with multiple pages if necessary)
        """
        #start with displaying top of the inventory
        #and retrieve id of next element to display
        next = self.displaySelection(0)
        print(next)
        #loop until exited from within
        while 1:
            key = getKeyInput()
            if key == self.keyMap['quit']:
                #exit the loop and finish displaying
                break
            #show next page of elements
            if key == self.keyMap['next']:
                next = self.displaySelection(next)
            #show previous page of elements
            if key == self.keyMap['prev']:
                pass

    def displaySelection(self, start):
        """
        display one page of items
        """
        #iteration counter
        i = start
        #check if id not out of range
        if not isSet(self.elements_, i):
            #reset id if necessary
            i = 0
        for char in charGen():
            #check if the end of the list is reached
            if not isSet(self.elements_, i):
                break
            #display element
            print(char + ': ' + str(self.elements_[i]))
            #iterate counter
            i += 1
        #if end of list was not reached during display
        else:
            #return the iterator indicating id of the element
            return i

        #return 0 indicating first element of the list is next to be displayed
        #resulting in kind-of rewind or wrap-around
        return 0