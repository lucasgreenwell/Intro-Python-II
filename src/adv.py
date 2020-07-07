from room import Room
from player import Player
from item import Item





# Declare all the rooms

rooms = {
    'outside':  Room("Outside",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

user = Player("Adventurer", "outside")
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

wants_to_play = True
while wants_to_play:
    user_input = input(f"Current Room: {user.current_room}. {rooms[user.current_room].room_description}. Pick a direction, N, E, S, or W. Press Q to exit ")
   #quitting
    if user_input.lower() == 'q' or user_input.lower() == "quit":
        wants_to_play = False

    #rules for Northern advance
    elif user_input.lower() == 'n':
        north_room = rooms[user.current_room].n_to
        if north_room != None:
            user.current_room = north_room.room_name.lower()
        else:
            user_input = input(f"You are not able to go that way. Pick a different direction. Current Room: {user.current_room}. {rooms[user.current_room].room_description}. Pick a direction, N, E, S, or W. Press Q to exit ")

    #south
    elif user_input.lower() == 's':
        south_room = rooms[user.current_room].s_to
        if south_room != None:
            user.current_room = south_room.room_name.lower()
        else:
            user_input = input(f"You are not able to go that way. Pick a different direction. Current Room: {user.current_room}. {rooms[user.current_room].room_description}. Pick a direction, N, E, S, or W. Press Q to exit ")

    #west
    elif user_input.lower() == 'w':
        west_room = rooms[user.current_room].w_to
        if west_room != None:
            user.current_room = west_room.room_name.lower()
        else:
            user_input = input(f"You are not able to go that way. Pick a different direction. Current Room: {user.current_room}. {rooms[user.current_room].room_description}. Pick a direction, N, E, S, or W. Press Q to exit ")


