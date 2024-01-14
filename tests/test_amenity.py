#!/usr/bin/python3
""" import unittest """
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ tests the amenity class """

    def test_name(self) -> None:
        """ tests the name attribute """
        the_amenity = Amenity()
        self.assertEqual(type(the_amenity.name), str)
