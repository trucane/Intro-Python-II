# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"My name is {self.name} and I am in room"

    def __repr__(self):
        return f"Player({repr(self.name)}"

    def move(self, direction):
        self.direction = direction
        if(direction != 'q'):
            if(direction == "n" or direction == "e" or direction == "s" or direction == "w"):
                if(getattr(self.current_room , f'{direction}_to') != None):
                    self.current_room = getattr(self.current_room , f'{direction}_to')
                else:
                    print('You went the wrong direction')
            else: 
                print(f'Sorry please select a correct direction')


