import unittest

from src.song import Song
from src.room import Room
from src.guest import Guest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("John")
        
    def test_guest_has_name(self):
        self.assertEqual(self.guest_1.first_name, self.guest_1.create_guest())