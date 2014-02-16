from unittest import TestCase
from engine.spatial import Spatial


class TestSpatial(TestCase):
    def test_get_route_to(self):
        test_object = Spatial(1, 1)

        # horizontal aim
        self.assertEqual(
            list(Spatial.get_route_to(test_object, 5, 1)),
            [[2, 1], [3, 1], [4, 1]]
        )
        # vertical aim
        self.assertEqual(
            list(Spatial.get_route_to(test_object, 1, 5)),
            [[1, 2], [1, 3], [1, 4]]
        )
        # aim at self
        self.assertEqual(
            list(Spatial.get_route_to(test_object, 1, 1)),
            [[1, 1]]
        )
        # diagonal aim
        self.assertEqual(
            list(Spatial.get_route_to(test_object, 5, 5)),
            [[2, 2], [3, 3], [4, 4]]
        )
        # negative diagonal aim
        self.assertEqual(
            list(Spatial.get_route_to(test_object, -4, -4)),
            [[0, 0], [-1, -1], [-2, -2], [-3, -3]]
        )
        # restricted aim
        self.assertEqual(
            list(Spatial.get_route_to(test_object, -4, -4, [[0, 0], [5, 5]])),
            [[0, 0]]
        )
        # aim at 22,5 degree
        self.assertEqual(
            list(Spatial.get_route_to(test_object, 2, 6)),
            [[1, 2], [1, 3], [2, 4], [2, 5]]
        )
        # another symmetric aim
        self.assertEqual(
            list(Spatial.get_route_to(test_object, 3, 6)),
            [[1, 2], [2, 3], [2, 4], [3, 5]]
        )
        # an asymmetric aim
        self.assertEqual(
            list(Spatial.get_route_to(test_object, 2, 5)),
            [[1, 2], [2, 3], [2, 4]]
        )
