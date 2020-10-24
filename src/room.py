class Room:

    def __init__(self, room_number, room_occupants, number_of_songs):
        self.room_number = room_number
        self.room_occupants = []
        self.number_of_songs = []

    def create_room(self):
        return self.room_number

    def add_occupants(self, guest):
        self.room_occupants.append(guest)

    def remove_occupants(self, guest):
        self.room_occupants.remove(guest)

    def add_song(self, music):
        self.number_of_songs.append(music)
    