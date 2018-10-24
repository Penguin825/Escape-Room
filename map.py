from items import *

room_cupboard = {
    "name": "Cupboard",

    "description":
    """You are currently stuck in a cupboard on the second floor of
a strange house. Your challenge is to overcome the obstacles and get
out of the house. The cupboard has an exit to the east and some wired
coat hangers in the corner of the room.""",

    #exits now have a boolean value to determine the locked condition
    "exits": {"east": ["Bedroom", False]},

    "items": [item_hanger]
}

room_bedroom = {
    "name": "Bedroom",

    "description":
    """You are standing in the middle of a bedroom. The cupboard is to the
west. There are doors to the south and east, but both are locked. With the
right tools, you may be able to pick one of the locks.""",

    "exits":  {"west": ["Cupboard", False] , "east": ["Bathroom", True, item_hanger],
               "south": ["Upstairs corridor", True, item_null]},

    "items": [item_lamp, item_guitar, item_rug]
}

room_bathroom = {
    "name": "Bathroom",

    "description":
    """You are now in a dirty bathroom. There is a sign on the wall above the sink and
several items scattered around. There's a second door to the south which looks so grimy
it cannot be opened.""",

    "exits": {"west": ["Bedroom", False], "south": ["Upstairs corridor", True, False]},

    "items": [item_mirror, item_sign, item_medicine, item_soap, item_toothbrush, item_mop]
}

room_corridor = {
    "name": "Upstairs corridor",

    "description":
    """You are now in the upstairs corridor. To the south there is a flight of stairs
going down. The stairs are blocked by a dog gate with a four-letter passcode lock. You
also wish that there is a cute dalmation dog somewhere nearby to comfort you. The exit
to the north leads back to the bedroom; to the east there is a door to a study with a
card scanner by the handle. There is a photo on the wall next to a poster and a really
cute dog painting on the wall. The longer you stare at the painting the more happy you
become.""",

    "exits": {"east": ["Study", True, item_id], "south": ["Stairs", True, "abra"],
              "north": ["Bedroom", True, item_null]},

    "items": [item_gate, item_poster, item_photo, item_painting]
}

room_study = {
    "name": "Study",

    "description":
    """You have now gained access to the study. The walls are lined with bookshelves: you
see a well-used book titled "Puns for the casual Java Developer: 23rd Edition" written by
one K. Siridov. There is a large desk in the centre of the room. The exit to the west leads
back to the upstairs corridor.""",

    "exits": {"west": ["Upstairs corridor", False]},

    "items": [item_notepad, item_key, item_folders, item_books]
}

room_stairs = {
    "name": "Stairs",

    "description":
    """You are on some fluffy carpeted stairs. You can go north back to the
upstairs corridor or south to the downstairs hallway. It looks like someone
has been doing repair work to the handrail and there are some tools scattered
around.""",

    "exits": {"north": ["Upstairs corridor", False], "south": ["Hallway", False]},

    "items": [item_hammer, item_screwdriver, item_crowbar, item_saw]
}

room_kitchen = {
    "name": "Kitchen",

    "description":
    """You are now in a kitchen. You are especially annoyed by the dirty
plates left on the breakfast bar. Who has been cooking eggs? Ew. You can
go east to return to the hallway. The door to the south seems to be jammed
shut at the moment.""",

    "exits": {"south": ["Dining room", True, item_crowbar], "east": ["Hallway", False]},

    "items": [item_plates, item_microwave]

}

room_dining = {
    "name": "Dining Room",

    "description":
    """You are now in a dining room. There is a alienware laptop on
the dining room table. Alienware? You think to yourself who in their
right mind would purchase that overpriced #£$%. There is also a pretty
vase of flowers; whoever picked those has good taste. The exit to the
north leads back to the kitchen.""",

    "exits": {"north": ["Kitchen", False]},

    "items": [item_laptop, item_mouse, item_flowers]

}

room_living = {
    "name": "Living Room",

    "description":
    """You are currently in a living room. There is one large corner sofa, a TV and
a coffee table. The coffee table has an ID card and a cold cup of tea left on it.
There is only one exit which is to the west and returns you to the hallway. It has
another one of those card scanners next to the lock and seems to have locked behind
you.""",

    "exits": {"west": ["Hallway", True, item_id]},

    "items": [item_sofa, item_tv, item_id, item_tea]

}

room_hallway = {
    "name": "Hallway",

    "description":
    """You are now in the downstairs hallway. There is an exit to the west which
leads to the living room. The exit to the east leads to the kitchen and
south there is the front door.""",

    "exits": {"east": ["Living room", False], "west": ["Kitchen", False],
              "south": ["Exit", True, item_key], "north": ["Stairs", False]},

    "items": []

}

room_exit = {
    "name": "Exit",

    "description":
    "",

    "exits": {},

    "items": []
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
