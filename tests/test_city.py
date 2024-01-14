#!/usr/bin/python3
""" import unittest """
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ tests the city class """

    def setUp(self) -> None:
        """ creates instance """
        self.my_city = City()

    def test_stateid(self) -> None:
        """ tests state_id """
        self.assertEqual(type(self.my_city.state_id), str)

    def test_name(self) -> None:
        """ tests the name attribute """
        self.assertEqual(type(self.my_city.name), str)
