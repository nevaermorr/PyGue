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
        obtain coordinate from x-axis
        """
        return self.x

    def get_y(self):
        """
        obtain coordinate from x-axis
        """
        return self.y

    def get_coordinates(self):
        """
        obtain spatial coordinates of the object
        """
        return [self.x, self.y]

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
                    yield [
                        self.x + i * sign(vector_x),
                        self.y + int(i * (vector_y + sign(vector_y)) / abs(vector_x))
                    ]

        else:
            for i in range(abs(vector_y)):
                if i != 0:
                    yield [
                        self.x + int(i * (vector_x + sign(vector_x)) / abs(vector_y)),
                        self.y + i * sign(vector_y)
                    ]

    def get_beam_route_to(self, x, y):
        """
        generate coordinates of points that are at least partially in route
        from this point to [x, y]
        :param x: horizontal coordinate of target point
        :param y: vertical coordinate of target point
        """
        # horizontal part of route vector
        vector_x = x - self.x
        # vertical part of route vector
        vector_y = y - self.y

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

        # along the route
        for i in range(max(abs(vector_x), abs(vector_y))):
            # omit the starting point
            if i == 0:
                continue
            # obtain all possible components of the vectors
            if int(i * dx) == i * dx:
                x_components_ = [int(i * dx)]
            else:
                x_components_ = [int(i * dx), int(i * dx) + sign(dx)]
            if int(i * dy) == i * dy:
                y_components_ = [int(i * dy)]
            else:
                y_components_ = [int(i * dy), int(i * dy) + sign(dy)]

            # combine components to points
            points_ = []
            for x in x_components_:
                for y in y_components_:
                    points_.append([self.x + x, self.y + y])
            # return proper alternative points
            yield points_

    def neighbours_with(self, x, y):
        """
        check if this object neighbours with another
        """
        return (
            x - 1 <= self.x <= x +1
            and y - 1 <= self.y <= y + 1
        )