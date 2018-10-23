from items import *

room_cupboard = {
    "name": "Cupboard",

    "description":
    """You are currently in a cupboard in a house you are stuck. Your
challenge is to overcome the obstacles and get out of the house.
The cupboard has an exit to the east and a pile of wired coat hangers
to the west.""",

    "exits": {"east": "Bedroom"},

    "items": [item_hanger]
}

room_bedroom = {
    "name": "Bedroom",

    "description":
    """You are stood in the middle of the bedroom. The exit to the west leads
you back into the cupboard. To the south is locked and cannot be
opened. The exit to the east leads to the bathroom but is also locked but can
be picked using wire.""",

    "exits":  {"west": "Cupboard" , "east": "Bathroom"},

    "items": [item_lamp, item_guitar, item_rug]
}

room_bathroom = {
    "name": "Bathroom",

    "description":
    """You are now in a dirty bathroom. There is a sign to the north that says KEEP
THIS BATHROOM CLEAN! Go west to re-enter the bedroom. The exit to the south
is an exit into the corridor.""",

    "exits": {"west": "Bedroom", "south": "Upstairs corridor"},

    "items": [item_sign, item_medicine, item_mirror, item_soap, item_toothbrush, item_mop]
}

room_corridor = {
    "name": "Upstairs corridor",

    "description":
    """You are now in the middle of the upstairs corridor. The exit to the south
are the stairs going downstairs. However, there is a dog patterned stair gate
with a four lettered lock code. The code to the stair gate is somewhere in the
corridor. There is also an exit to the north leading to the bedroom; to the
east there is a door to the study but it is only accessible using a card touch
pad. There is a a dog painting on the west wall.""",

    "exits": {"east": "Study", "south": "Stairs", "north": "Bedroom"},

    "items": [item_painting]
}

room_study = {
    "name": "Study",

    "description":
    """You have now accessed the study. The walls are lined with book shelves and there
is a desk in the centre of the room. There is an exit to the west to return into
the upstairs corridor.""",

    "exits": {"west": "Upstairs corridor"},

    "items": [item_notepad, item_key, item_folders]
}

room_stairs = {
    "name": "Stairs",

    "description":
    """You are on the stairs. Go north to the upstairs corridor or south to the
downstairs hallway.""",

    "exits": {"north": "Upstairs corridor", "south": "Hallway"},

    "items": []
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """You are now in the kitchen. There is a crow bar and some dirty plates on the
breakfast bar. Go east to return to the hallway. The exit to the south leads to
dining room and is currently jammed and therefore needs to be forced open.""",

    "exits": {"south": "Dining Room", "east": "Hallway"},

    "items": [item_crowbar, item_plates]

}

room_dining = {
    "name": "Dining Room",

    "description":
    """ You are now in the living room. There is a laptop on the dining room
table as well as a vase of flowers. There is an exit to the north which leads
to the kitchen.""",

    "exits": {"north": "Kitchen"},

    "items": [item_laptop, item_flowers]

}

room_living = {
    "name": "Living Room",

    "description":
    """You are currently in the living room. There are two sofas, a TV and
a coffee table. The coffe table has an ID card and a cup of tea. There is only
one exit which is to the west and returns you to the hallway.""",

    "exits": {"west": "Hallway"},

    "items": [item_id, item_tea]

}

room_hallway = {
    "name": "Hallway",

    "description":
    """You are now in the downstairs hallway. There is an exit to the west which
leads to the lvining room. The exit to the east leads to the kitchen and to the
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
