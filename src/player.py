# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room,):
        self.name = name
        self.inventory = inventory
        self.current_room = current_room

    def _str_(self):
        return f"My name is {self.name} and I am in room {self.current_room}"

    def __repr__(self):
        return f"Player({repr(self.name)}, {repr(self.current_room)})"


        