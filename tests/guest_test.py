import unittest

from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("John")

    def test_guest_is_created(self):
        self.assertEqual(self.guest.first_name, self.guest.create_guest())