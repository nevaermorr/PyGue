from utilities.generalFunctions import *


class Spatial():
    """
    any element placed in the space
    """

    def __init__(self, x, y):
        # horizontal coordinate
        self.x = x
        # vertical coordinate
        self.y = y

    def get_x(self):
        """
        get coordinate from x-axis
        """
        return self.x

    def get_y(self):
        """
        get coordinate from x-axis
        """
        return self.y

    def get_route_to(self, x, y):
        """
        generate coordinates of subsequent points of route from this point to [x, y]
        :param x: horizontal coordinate of target point
        :param y: vertical coordinate of target point
        """
        # horizontal part of route vector
        vector_x = x - self.x
        # vertical part of route vector
        vector_y = y - self.y

#pprint('----------')
#print('target:')
#pprint([x, y])
#print('start:')
#pprint([self.x, self.y])
#print('vector:')
#pprint([vector_x, vector_y])

        # calculate the steps
        if vector_x == 0 and vector_y == 0:
            dx = 0
            dy = 0
        elif abs(vector_x) >= abs(vector_y):
            dx = sign(vector_x)
            dy = sign(vector_y) * abs(vector_y / vector_x)
        else:
            dx = sign(vector_x) * abs(vector_x / vector_y)
            dy = sign(vector_y)

#print('step:')
#pprint([dx, dy])
#print('number of steps:')
#pprint(max(vector_x, vector_y))
        # round the values to integers
        for i in range(max(abs(vector_x), abs(vector_y))):
#pprint([int(self.x + i * dx), int(self.y + i * dy)])
            yield int(self.x + i * dx), int(self.y + i * dy)