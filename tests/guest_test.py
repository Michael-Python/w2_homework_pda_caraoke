import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest1 = Guest("John")
        self.guest2 = Guest("Sally")
        self.guest3 = Guest("Bill")
        self.guest4 = Guest("Wendy")

    def test_guest_has_name(self):
        self.assertEqual(self.guest2.first_name, self.guest2.create_guest())