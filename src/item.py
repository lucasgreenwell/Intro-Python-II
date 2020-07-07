class Item:
    def __init__(self, item_name, item_description, current_room = None, held_by = None):
        self.item_name = item_name
        self.item_description = item_description
        self.current_room = current_room
        self.held_by = held_by

    def __str__(self):
        return f"<{self.item_name}: {self.item_description}"

    def on_take(self, player):
        self.held_by = player
        self.current_room = None

    def on_drop(self, current_room):
        self.held_by = None
        self.current_room = current_room