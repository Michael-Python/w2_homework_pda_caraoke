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
        # this takes one element from songs and appends the empty list from each song from the loop
        number_of_songs = [self.number_of_songs.append(song) for song in songs]
            
    # def put_all_guests_in_room(self, guests):
    #     self.room_occupants = [self.room_occupants.append(guest) for guest in guests]
    #     return len(self.room_occupants)

    # def check_if_room_is_full__is_full(self, guests):
    #     self.room_occupants = []
    #     for guest in guests:
    #         if len(self.room_occupants) > self.rooms[0].max_occupancy:
    #         # if len(self.room_occupants) > 4:
    #             return("This room is full!")
    #         else: 
        #         self.room_occupants.append(guest)
        # return("There is space available.")
        
    def check_if_room_is_full(self, guests):        
        for guest in guests:
            if len(self.room_occupants) > self.max_occupancy:
            # if len(self.room_occupants) > self.max_occupancy:
            # if len(self.room_occupants) > 7:
                return("This room is full!")
            else: 
                self.room_occupants.append(guest)
        return("There is space available.")
        

    