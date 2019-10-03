# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, ):
        self.name = name
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.description = description

    def __str__(self):
        return f"You are in room {self.name} the {self.description}"

    def __repr__(self):
        return f"Room({repr(self.name)}, {repr(self.description)})"