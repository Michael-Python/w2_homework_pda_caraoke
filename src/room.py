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
                  
    def check_if_room_is_full(self, guests):        
        for guest in guests:
            if len(self.room_occupants) > self.max_occupancy:
                print(f"You can only have {self.max_occupancy} guests in {self.room_number}.")
                return("This room is full!")
            else: 
                self.room_occupants.append(guest)
        print(f"There is space for all the guests in {self.room_number}.")
        return("There is space available.")

    def check_if_guests_can_pay(self, guests):
        for guest in guests:
            if self.fee > guest.wallet:
                print(f"You cannot all afford to sing in {self.room_number}.")
                return "You cannot all afford it." 
            else:
                self.room_occupants.append(guest)
        print(f"Everyone can afford to sing in {self.room_number}.")
        return "You can all afford it."
