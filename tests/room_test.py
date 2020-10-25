import unittest

from src.song import Song
from src.room import Room
from src.guest import Guest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("John", 10)
        self.guest_2 = Guest("Sally", 20)
        self.guest_3 = Guest("Bill", 15)
        self.guest_4 = Guest("Wendy", 5)
        self.guest_5 = Guest("Tom", 30)
        self.guest_6 = Guest("Becky", 12)
        self.guest_7 = Guest("Sheila", 99)


        self.room_1 = Room("Room 1", 10, 4, 0, 0)
        # self.room_2 - Room("Room 2", 20, 5, 0, 0)
        # self.room_3 = Room("Room 3", 15, 6, 0, 0)


        self.song_1 = {"number" : 1, "title" : "Waterloo", "artist" : "Abba", "genre" : "Disco"}
        self.song_2 = {"number" : 2, "title" : "Staying Alive", "artist" : "The BeeGees", "genre" : "Disco"}
        self.song_3 = {"number" : 3, "title" : "Better Man", "artist" : "Pearl Jam", "genre" : "Alternative"}
        self.song_4 = {"number" : 4, "title" : "Black Hole Sun", "artist" : "Soundgarden", "genre" : "Alternative"}
        self.song_5 = {"number" : 5, "title" : "This Flight Tonight", "artist" : "Nazareth", "genre" : "Rock"}
        self.song_6 = {"number" : 6, "title" : "The Chain", "artist" : "Fleetwood Mac", "genre" : "Rock"}
        
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
        self.assertEqual(self.room_1.room_number, self.room_1.create_room())

    def test_is_room__empty(self):
        self.assertEqual(0, len(self.room_1.room_occupants))

    def test_is_room__not_empty(self):
        self.room_1.add_occupants(self.guest_1)
        self.room_1.add_occupants(self.guest_2)
        self.room_1.add_occupants(self.guest_3)
        self.room_1.add_occupants(self.guest_4)
        self.assertEqual(4, len(self.room_1.room_occupants))

    def test_is_room__empty_now(self):
        self.room_1.add_occupants(self.guest_1)
        self.room_1.remove_occupants()
        self.assertEqual(0, len(self.room_1.room_occupants))


    def test_is_song_added(self):
        self.room_1.add_song(self.songs)
        self.assertEqual(1, len(self.room_1.number_of_songs))

    def test_list_had_additions(self):
        self.room_1.add_song_to_list(self.songs)
        self.assertEqual(6, len(self.room_1.number_of_songs))
