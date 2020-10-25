import unittest

from src.song import Song
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("John", 10)
        self.guest_2 = Guest("Sally", 20)
        self.guest_3 = Guest("Bill", 15)
        self.guest_4 = Guest("Wendy", 0)

        self.room = Room("Room 1", 0, 0)

        self.song = Song("Waterloo", "Abba", "Disco")

        # self.song = [
        #     {"name" : "Waterloo", "band" : "Abba", "genre" : "Disco"}
        #     {"name" : "Staying Alive", "band" : "The BeeGees", "genre" : "Disco"}
        #     {"name" : "Better Man", "band" : "Pearl Jam", "genre" : "Alternative"}
        #     {"name" : "Black Hole Sun", "band" : "Soundgarden", "genre" : "Alternative"}
        #     {"name" : "This Flight Tonight", "band" : "Nazareth", "genre" : "Rock"}
        #     {"name" : "The Chain", "band" : "Fleetwood Mac", "genre" : "Rock"}
        # ]
        # self.song_1 = Song("Waterloo", "Abba", "Disco")
        # self.song_2 = Song("Staying Alive", "The BeeGees", "Disco")
        # self.song_3 = Song("Better Man", "Pearl Jam", "Alternative")
        # self.song_4 = Song("Black Hole Sun", "Soundgarden", "Alternative")
        # self.song_5 = Song("This Flight Tonight", "Nazareth", "Rock")
        # self.song_6 = Song("The Chain", "Fleetwood Mac", "Rock")

    def test_room_is_created(self):
        self.assertEqual(self.room.room_number, self.room.create_room())

    def test_is_room__empty(self):
        self.assertEqual(0, len(self.room.room_occupants))

    def test_is_room__not_empty(self):
        self.room.add_occupants(self.guest_1)
        self.room.add_occupants(self.guest_2)
        self.room.add_occupants(self.guest_3)
        self.room.add_occupants(self.guest_4)
        self.assertEqual(4, len(self.room.room_occupants))

    def test_is_room__empty_now(self):
        self.room.add_occupants(self.guest_1)
        self.room.remove_occupants(self.guest_1)
        self.assertEqual(0, len(self.room.room_occupants))
    
    def test_is_song_added(self):
        self.room.add_song(self.song)
        self.assertEqual("Waterloo", self.song.title)
        self.assertEqual(1, len(self.room.number_of_songs))