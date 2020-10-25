class Guest:
    def __init__(self, first_name, wallet):
        self.first_name = first_name
        self.wallet = wallet
        
    def create_guest(self):
        return self.first_name