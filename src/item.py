class Item:
    def __init__(self, item_name, item_description, current_location = None, held_by = None):
        self.item_name = item_name
        self.item_description = item_description
        self.current_location = current_location
        self.held_by = held_by

    def __str__(self):
        return f"<{self.item_name}: {self.item_description}"

    def on_take(self, player):
        self.held_by = player
        self.current_location = None
