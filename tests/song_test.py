import unittest

from src.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        # this links to file song, class Song and the three parameters of title, artist and genre
        self.song = Song("Waterloo", "Abba", "Disco")

    def test_song_is_added(self):
        # This checks that the title passed to self.song.title ("Waterloo" above) matches with the function in the file song called, create_song
        self.assertEqual(self.song.title, self.song.add_song())

    