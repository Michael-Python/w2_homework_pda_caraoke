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

        self.room_1 = Room("Room 1", 0, 0, 4)
        self.room_3 - Room("Room 2", 0, 0, 5)
        self.room_3 = Room("Room 3", 0, 0, 62)


        self.song_1 = Song(1, "Waterloo", "Abba", "Disco")
        self.song_2 = Song(2, "Staying Alive", "The BeeGees", "Disco")
        self.song_3 = Song(3, "Better Man", "Pearl Jam", "Alternative")
        self.song_4 = Song(4, "Black Hole Sun", "Soundgarden", "Alternative")
        self.song_5 = Song(5, "This Flight Tonight", "Nazareth", "Rock")
        self.song_6 = Song(6, "The Chain", "Fleetwood Mac", "Rock")
        
        self.songs = [self.song_1, self.song_2, self.song_3, self.song_4, self.song_5, self.song_6]

        # self.song = [
        #     {"name" : "Waterloo", "band" : "Abba", "genre" : "Disco"}
        #     {"name" : "Staying Alive", "band" : "The BeeGees", "genre" : "Disco"}
        #     {"name" : "Better Man", "band" : "Pearl Jam", "genre" : "Alternative"}
        #     {"name" : "Black Hole Sun", "band" : "Soundgarden", "genre" : "Alternative"}
        #     {"name" : "This Flight Tonight", "band" : "Nazareth", "genre" : "Rock"}
        #     {"name" : "The Chain", "band" : "Fleetwood Mac", "genre" : "Rock"}
        # ]
        

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

    def test_is_song_added(self):
        self.room.add_song(self.songs)
        self.assertEqual("Black Hole Sun", self.song_4.title)
        self.assertEqual(1, len(self.room.number_of_songs))