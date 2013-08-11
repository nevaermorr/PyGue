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
        #internal pointer - id of first element after currently displayed
        self.pointer = 0

    def displayElements(self):
        """
        display elements of this list (with multiple pages if necessary)
        """
        #start with displaying top of the inventory
        self.displaySelection(self.pointer)
        #loop until exited from within
        while 1:
            key = getKeyInput()
            if key == self.keyMap['quit']:
                #reset internal pointer
                self.pointer = 0
                #exit the loop and finish displaying
                break
            #show next page of elements
            if key == self.keyMap['next']:
                self.displaySelection('next')
            #show previous page of elements
            if key == self.keyMap['prev']:
                pass

    def displaySelection(self, dir = 'next'):
        """
        display one page of items
        :param dir: direction of displaying - next or prev
        """
        #TODO direction of displaying
        #selection of elements to display
        selection_ = []
        #check if pointer is in range
        self.validatePointer()
        #iterate character labels
        for char in charGen():
            #check if the end of the list is reached
            if not self.validatePointer():
                break
            #display element
            selection_.append(char + ': ' + str(self.elements_[self.pointer]))
            #iterate counter
            self.pointer += 1

        #display extracted selection
        for element in selection_:
            print(element)

    def validatePointer(self):
        """
        check there is an element in list corresponding to internal pointer
        """
        #check if pointer is not out of range
        if not isSet(self.elements_, self.pointer):
            #reset pointer if necessary
            self.pointer = 0
            return False
        else:
            return True