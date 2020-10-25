class Room:

    def __init__(self, room_number, fee, max_occupancy,  room_occupants, number_of_songs):
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

    def add_song_to_list(self, songs):
        # this takes one element from songs
        for song in songs:
            # this appends the empty list from each song from the loop
            self.number_of_songs.append(song)

    # def check_if_room_is_full(self, guest):
    #     self.room_occupants = 0
    #     for guest in guests:
    #         self.room_occupants.append(guest)
    #         print(guest)
    #     return len(self.room_occupants)

    