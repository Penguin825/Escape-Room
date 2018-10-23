from items import *

room_cupboard = {
    "name": "Cupboard",

    "description":
    """You are currently stuck in a cupboard on the second floor of
a strange house. Your challenge is to overcome the obstacles and get
out of the house. The cupboard has an exit to the east and some wired
coat hangers in the corner of the room.""",

    "exits": {"east": ["Bedroom", False]},

    "items": [item_hanger]
}

room_bedroom = {
    "name": "Bedroom",

    "description":
    """You are standing in the middle of a bedroom. There is an exit to
the west which leads you back into the cupboard. To the south is another
door which cannot be opened. The exit to the east leads to what looks like
an ensuite bathroom, this door is also locked. With the right tools this door can
be picked.""",

    "exits":  {"west": ["Cupboard", False] , "east": ["Bathroom", True, item_hanger],
               "south": ["Upstairs corridor", True, item_null]},

    "items": []
}

room_bathroom = {
    "name": "Bathroom",

    "description":
    """You are now in a dirty bathroom. There is a sign on the tiled wall that says
KEEP THIS BATHROOM CLEAN OR ELSE! West leads back to the bedroom. The exit to the south
is an exit into a corridor.""",

    "exits": {"west": ["Bedroom", False], "south": ["Upstairs corridor", True, False]},

    "items": [item_sign, item_soap]
}

room_corridor = {
    "name": "Upstairs corridor",

    "description":
    """You are now in the middle of the upstairs corridor. The exit to the south
is a flight of stairs going down. However, there is a dalmatian patterned stair gate
with a four lettered lock code. You also wish that there is a cute dalmation dog somewhere
to comfort you. The code to the stair gate could be somewhere in the
corridor. The exit to the north leads back to the bedroom; to the
east there is a door to a study but it is only accessible using a smart card. There is a
photo on the wall next to a poster. There is also a really cute dog painting on the wall,
the longer you stare at the painting the more happy you become.""",

    "exits": {"east": ["Study", True, item_id], "south": ["Stairs", True, "abra"],
              "north": ["Bedroom", True, item_null]},

    "items": [item_painting, item_poster, item_photo, item_gate]
}

room_study = {
    "name": "Study",

    "description":
    """You have now gained access to the study. The walls are lined with book shelves,
you see alot of books named 'Java Puns', you are definitely better off not
reading them. There is a large desk in the centre of the room. The exit to the west
leads back to the upstairs corridoor.""",

    "exits": {"west": ["Upstairs corridor", False]},

    "items": [item_notepad, item_key, item_books]
}

room_stairs = {
    "name": "Stairs",

    "description":
    """You are on the fluffy carpeted stairs. You can go north back to the
upstairs corridor or south to the eerie downstairs hallway.""",

    "exits": {"north": ["Upstairs corridor", False], "south": ["Hallway", False]},

    "items": []
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """You are now in a kitchen. You are especially annoyed by the dirty
plates left on the breakfast bar, also why is there a crowbar here? You can
go east to return to the hallway. The exit to the south leads to a dining room
and is currently jammed.""",

    "exits": {"south": ["Dining room", True, item_crowbar], "east": ["Hallway", False]},

    "items": [item_crowbar, item_plates]

}

room_dining = {
    "name": "Dining Room",

    "description":
    """You are now in a dining room. There is a alienware laptop on
the dining room table. Alienware? You think to yourself who in their
right mind would purchase that overpriced #£$%. There is also a pretty vase of flowers,
whoever picked those has good taste. The exit to the north leads back to the kitchen.""",

    "exits": {"north": ["Kitchen", False]},

    "items": [item_laptop, item_flowers]

}

room_living = {
    "name": "Living Room",

    "description":
    """You are currently in a living room. There is one large corner sofa, a TV and
a coffee table. The coffee table has an ID card and a cold cup of tea left on it.
There is only one exit which is to the west and returns you to the hallway.""",

    "exits": {"west": ["Hallway", True, item_id]},

    "items": [item_id, item_tea]

}

room_hallway = {
    "name": "Hallway",

    "description":
    """You are now in the downstairs hallway. There is an exit to the west which
leads to the living room. The exit to the east leads to the kitchen and
south there is the front door. However, the front door is locked and cannot be 
opened without a key.""",

    "exits": {"east": ["Living room", False], "west": ["Kitchen", False],
              "south": ["Exit", True, item_key], "north": ["Stairs", False]},

    "items": []

}

room_exit = {
    "name": "Exit",

    "description":
    """CONGRATULATIONS

You escaped the house!""",

    "exits": {},

    "items": [item_freedom]
}

rooms = {
    "Cupboard": room_cupboard,
    "Bedroom": room_bedroom,
    "Bathroom": room_bathroom,
    "Upstairs corridor": room_corridor,
    "Study": room_study,
    "Stairs": room_stairs,
    "Kitchen": room_kitchen,
    "Living room": room_living,
    "Dining room": room_dining,
    "Hallway": room_hallway,
    "Exit": room_exit
}
