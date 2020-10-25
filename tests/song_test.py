import unittest

from src.song import Song
from src.room import Room
from src.guest import Guest


class TestSong(unittest.TestCase):

    def setUp(self):
        # this links to file song, class Song and the three parameters of title, artist and genre
        self.song_1 = Song(1, "Waterloo", "Abba", "Disco")

    def test_info_is_added(self):
        # This checks that the title, artist and genre passed to self.song.title ("Waterloo", "Abba", "Disco" above) matches with the function in the file song called, create_song
        self.assertEqual("Waterloo", self.song_1.add_song())
        self.assertEqual("Abba", self.song_1.add_artist())
        self.assertEqual("Disco", self.song_1.add_genre())
