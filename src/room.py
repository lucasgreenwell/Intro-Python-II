# Implement a class to hold room information. This should have name and
# description attributes.

# Put the Room class in room.py based on what you see in adv.py.
#
# The room should have name and description attributes.
#
# The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.
class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description


        # Need to set these explicitly when calling the room constructor
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None
        self.items = []

    def __str__ (self):
        return f"{self.name}: {self.description}"

