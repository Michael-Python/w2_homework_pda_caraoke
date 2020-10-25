import unittest

from src.song import Song
from src.room import Room
from src.guest import Guest


class TestSong(unittest.TestCase):

    def setUp(self):
        # this links to file song, class Song and the three parameters of title, artist and genre
        self.song = Song("Waterloo", "Abba", "Disco")

    def test_song_is_added(self):
        # This checks that the title, artist and genre passed to self.song.title ("Waterloo", "Abba", "Disco" above) matches with the function in the file song called, create_song
        self.assertEqual(self.song.title, self.song.add_song())
        self.assertEqual(self.song.artist, self.song.add_artist())
        self.assertEqual(self.song.genre, self.song.add_genre())
