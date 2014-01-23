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

    def get_route_to(self, x, y, debug = False):
        """
        generate coordinates of subsequent points of route from this point to [x, y]
        :param x: horizontal coordinate of target point
        :param y: vertical coordinate of target point
        """
        # horizontal part of route vector
        vector_x = x - self.x
        # vertical part of route vector
        vector_y = y - self.y

        # trivial case
        if vector_x == 0 and vector_y == 0:
            yield self.x, self.y
        # only vertical
        if vector_x == 0:
            for i in range(abs(vector_y) - 1):
                yield self.x, self.y + sign(vector_y) * (i + 1)
        # only horizontal
        elif vector_y == 0:
            for i in range(abs(vector_x) - 1):
                yield self.x + sign(vector_x) * (i + 1), self.y

        elif abs(vector_x) > abs(vector_y):
            for i in range(abs(vector_x)):
                if i != 0:
                    yield self.x + i * sign(vector_x),\
                        self.y + int(i*(vector_y + 1) / abs(vector_x))

        else:
            for i in range(abs(vector_y)):
                if i != 0:
                    yield self.x + int(i * (vector_x + 1) / abs(vector_y)),\
                        self.y + i * sign(vector_y)