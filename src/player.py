# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, player_name, current_room, inventory = []):
        self.current_room = current_room
        self.player_name = player_name
        self.inventory = inventory

    def __str__(self):
        return f"{self.player_name} is in  {self.current_room}"

    def get_item(self, item):
        self.inventory.append(item)

    def lose_item(self, item):
        self.inventory.remove(item)



