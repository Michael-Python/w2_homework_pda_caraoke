class Room:

    def __init__(self, room_number, room_occupants, fee, max_occupancy,  number_of_songs):
        self.room_number = room_number
        self.fee = fee
        self.max_occupancy = max_occupancy
        self.room_occupants = []
        self.number_of_songs = []
        
    def create_room(self):
        return self.room_number

    def add_occupants(self, guest):
        self.room_occupants.append(guest)

    def remove_occupants(self):
        self.room_occupants.clear()

    def add_song(self, music):
        self.number_of_songs.append(music)

    # def add_song(self, song):
    #     for song in self.songs
    #         return song

    # def check_if_room_is_full(self, guest):
    #     self.room_occupants = []
    #     for guest in guests:
    #         self.room_occupants.append(guest)
    #         print(guest)
    #     return len(self.room_occupants)

    