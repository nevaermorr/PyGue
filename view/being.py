from generalFunctions import *
from view.entity import *


class BeingView(EntityView):
    """
    display of being
    """

    def __init__(self, model):
        #parent constructor
        EntityView.__init__(self, model)

