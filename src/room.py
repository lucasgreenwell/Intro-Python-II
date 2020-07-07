# Implement a class to hold room information. This should have name and
# description attributes.

# Put the Room class in room.py based on what you see in adv.py.
#
# The room should have name and description attributes.
#
# The room should also have n_to, s_to, e_to, and w_to attributes which point to the room in that respective direction.
class Room:
    def __init__(self, room_name, room_description, items_inside = None):
        self.room_name = room_name
        self.room_description = room_description
        self.items_inside = items_inside

        # Need to set these explicitly when calling the room constructor
        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None


    def __str__(self):
        return f"{self.room_name}: {self.room_description}"
