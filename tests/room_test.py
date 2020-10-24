import unittest

from src.song import Song
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("John")
        self.guest_2 = Guest("Sally")
        self.guest_3 = Guest("Bill")
        self.guest_4 = Guest("Wendy")

        self.room = Room("Room 1", 0, 0)

        self.song = Song("Waterloo", "Abba", "Disco")

    def test_room_is_created(self):
        self.assertEqual(self.room.room_number, self.room.create_room())

    def test_is_room__empty(self):
        self.assertEqual(0, len(self.room.room_occupants))

    def test_is_room__not_empty(self):
        new_occupant = self.guest_1
        self.room.add_occupants(new_occupant)
        self.assertEqual(1, len(self.room.room_occupants))

    def test_is_room__empty_now(self):
        new_occupant = self.guest_1
        self.room.add_occupants(new_occupant)
        self.room.remove_occupants(new_occupant)
        self.assertEqual(0, len(self.room.room_occupants))
    
    def test_is_song_added(self):
        new_song = self.song
        self.room.add_song(new_song)
        self.assertEqual(1, len(self.room.number_of_songs))