from utilities.general_functions import *


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

    def get_route_to(self, x, y, max_area_=False):
        """
        generate coordinates of subsequent points of route from this point to [x, y]
        :param x: horizontal coordinate of target point
        :param y: vertical coordinate of target point
        :param max_area_: maximal size of area from which coordinates are desired
        as [[x_min, y_min], [x_max, y_max]]
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
                result_ = [self.x, self.y + sign(vector_y) * (i + 1)]
                # stop if the route stepped outside the area
                if max_area_ and not Spatial.in_area(result_, max_area_):
                    break
                yield result_
        # only horizontal
        elif vector_y == 0:
            for i in range(abs(vector_x) - 1):
                result_ = [self.x + sign(vector_x) * (i + 1), self.y]
                # stop if the route stepped outside the area
                if max_area_ and not Spatial.in_area(result_, max_area_):
                    break
                yield result_
        # every other case is nontrivial
        else:
            for step_ in self.get_nontrivial_route_by([vector_x, vector_y], max_area_):
                yield step_

    def get_nontrivial_route_by(self, vector_, max_area_):
        """
        generate coordinates of subsequent points of nontrivial route from this point to [x, y]
        :param vector_: vector to target point as [x_coordinate, y_coordinate]
        :param max_area_: maximal size of area from which coordinates are desired
        as [[x_min, y_min], [x_max, y_max]]
        """
        # local copy of route's starting point is needed
        start_ = [self.x, self.y]
        # the first coordinate has to be the longer one - reverse if necessary
        reverse = abs(vector_[1]) > abs(vector_[0])
        if reverse:
            vector_.reverse()
            start_.reverse()

        for i in range(abs(vector_[0])):
            if i != 0:
                result_ = [
                    start_[0] + i * sign(vector_[0]),
                    start_[1] + int(i * (vector_[1] + sign(vector_[1])) / abs(vector_[0]))
                ]
                # revert result if necessary
                if reverse:
                    result_.reverse()

                # stop if result is outside the desired area
                if not max_area_ or Spatial.in_area(result_, max_area_):
                    yield result_

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
            x_components_ = [int(i * dx)]
            if int(i * dx) != i * dx:
                x_components_.append(int(i * dx) + sign(dx))
            y_components_ = [int(i * dy)]
            if int(i * dy) != i * dy:
                y_components_.append(int(i * dy) + sign(dy))

            # combine components to points
            points_ = []
            for x in x_components_:
                for y in y_components_:
                    points_.append([self.x + x, self.y + y])
            # return proper alternative points
            yield points_

    def neighbours_with(self, x, y):
        """
        verify if this space point is adjacent to another
        :param x: horizontal coordinate of the other space point
        :param y: vertical coordinate of the other space point
        """
        return (
            x - 1 <= self.x <= x + 1
            and y - 1 <= self.y <= y + 1
        )

    @staticmethod
    def in_area(point_, area_):
        """
        verify if given point lies within given area
        :param point_: coordinates of a point as [x, y]
        :param area_: list of coordinates of extreme corners of area
        as [[x_min, y_min], [x_max, y_max]]
        """

        return (
            area_[0][0] <= point_[0] <= area_[1][0]
            and area_[0][1] <= point_[1] <= area_[1][1]
        )
