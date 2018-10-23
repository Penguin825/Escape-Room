from items import *

room_cupboard = {
    "name": "Cupboard",

    "description":
    """You are currently stuck in a cupboard on the second floor of
a strange house. Your challenge is to overcome the obstacles and get
out of the house. The cupboard has an exit to the east and some wired
coat hangers in the corner of the room.""",

    "exits": {"east": "Bedroom"},

    "items": [item_hanger]
}

room_bedroom = {
    "name": "Bedroom",

    "description":
    """You are standing in the middle of a bedroom. There is an exit to
the west which leads you back into the cupboard. To the south is another
door which cannot be opened. The exit to the east leads to what looks like
an on-suit bathroom, this door is also locked. With the right tools this door can
be picked.""",

    "exits":  {"west": "Cupboard" , "east": "Bathroom"},

    "items": []
}

room_bathroom = {
    "name": "Bathroom",

    "description":
    """You are now in a dirty bathroom. There is a sign on the tiled wall that says
KEEP THIS BATHROOM CLEAN OR ESLE! West leads back to the bedroom. The exit to the south
is an exit into a corridor.""",

    "exits": {"west": "Bedroom", "south": "Upstairs corridor"},

    "items": [item_sign]
}

room_corridor = {
    "name": "Upstairs corridor",

    "description":
    """You are now in the middle of the upstairs corridor. The exit to the south
is a flight of stairs going down. However, there is a dalmatian patterned stair gate
with a four lettered lock code. You also wish that there is a cute dalmation dog somewhere
to comfort you. The code to the stair gate could be somewhere in the
corridor. The exit to the north leads back to the bedroom; to the
east there is a door to a study but it is only accessible using a smart card.
There is also a really cute dog painting on the wall, The longer you stare at the painting
the more happy you become.""",

    "exits": {"east": "Study", "south": "Stairs", "north": "Bedroom"},

    "items": [item_painting]
}

room_study = {
    "name": "Study",

    "description":
    """You have now gained access to the study. The walls are lined with book shelves,
you see alot of books named 'Java Puns', you are definitely better off not reading them. There
is a large desk in the centre of the room. The exit to the west leads back to the
upstairs corridoor.""",

    "exits": {"west": "Upstairs corridor"},

    "items": [item_notepad, item_key]
}

room_stairs = {
    "name": "Stairs",

    "description":
    """You are on the fluffy carpeted stairs. You can go north back to the
upstairs corridor or south to the eerie downstairs hallway.""",

    "exits": {"north": "Upstairs corridor", "south": "Hallway"},

    "items": []
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """You are now in a kitchen. You are especially annoyed by the dirty
plates left on the breakfast bar, also why is there a crowbar here? You can
go east to return to the hallway. The exit to the south leads to a dining room
and is currently jammed, maybe it can be forced open.""",

    "exits": {"south": "Dining Room", "east": "Hallway"},

    "items": [item_crowbar, item_plates]

}

room_dining = {
    "name": "Dining Room",

    "description":
    """You are now in a dining room. There is a alienware laptop on
the dining room table. Alienware? You think to yourself who in their
right mind would purchase that overpriced #£$%. There is also a pretty vase of flowers,
whoever picked those has good taste. The exit to the north leads back to the kitchen.""",

    "exits": {"north": "Kitchen"},

    "items": [item_laptop, item_flowers]

}

room_living = {
    "name": "Living Room",

    "description":
    """You are currently in a living room. There is one large corner sofa, a TV and
a coffee table. The coffe table has an ID card and a cold cup of tea left on it.
There is only one exit which is to the west and returns you to the hallway.""",

    "exits": {"west": "Hallway"},

    "items": [item_id, item_tea]

}

room_hallway = {
    "name": "Hallway",

    "description":
    """You are now in the downstairs hallway. There is an exit to the west which
leads to the living room. The exit to the east leads to the kitchen and
south there is the front door. However, the front door is locked and cannot be 
opened without key.""",

    "exits": {"west": "Living Room", "east": "Kitchen"},

    "items": [item_frontdoor]

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
}
