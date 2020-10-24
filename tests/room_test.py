import unittest

from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1", 0)

    def test_room_is_created(self):
        self.assertEqual("Room 1", self.room.create_room())