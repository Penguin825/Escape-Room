#!/usr/bin/python3

import time

from map import rooms
from player import *
from items import *
from gameparser import *
from scoreboard import *
import sys
from time import sleep
global game_id


def start_menu():
    
    ascii = """

        ███████╗███████╗ ██████╗ █████╗ ██████╗ ███████╗    ██████╗  ██████╗  ██████╗ ███╗   ███╗
        ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝    ██╔══██╗██╔═══██╗██╔═══██╗████╗ ████║
        █████╗  ███████╗██║     ███████║██████╔╝█████╗      ██████╔╝██║   ██║██║   ██║██╔████╔██║
        ██╔══╝  ╚════██║██║     ██╔══██║██╔═══╝ ██╔══╝      ██╔══██╗██║   ██║██║   ██║██║╚██╔╝██║
        ███████╗███████║╚██████╗██║  ██║██║     ███████╗    ██║  ██║╚██████╔╝╚██████╔╝██║ ╚═╝ ██║
        ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝     ╚══════╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝
                                                                                         


    """

    about = """A puzzle game where you must solve the clues to escape your neighbour's house before they get home.
                                \n\n
    """

    menu = """
                          PRESS ANY KEY IF YOU WISH TO CONTINUE
                                  enter -99 to exit


                                      SCOREBOARD:
    """

    # Display ascii art
    for char in ascii:
        sleep(0.005)
        sys.stdout.write(char)
        sys.stdout.flush()

    # Display the game's about
    for char in about:
        sleep(0.023)
        sys.stdout.write(char)
        sys.stdout.flush()

    # Display the menu
    for char in menu:
        sleep(0.03)
        sys.stdout.write(char)
        sys.stdout.flush()

    print("\t\t\t\t" , "NAME" , "\t\t" , "TIME(s)")

    # Opens up scoreboard
    scoreboard()

    # Prompt input from user to start the game
    user_input = input("> ")
    if user_input == str(-99):
            quit()

    global game_id
    game_id =""

    # Making sure the name is limtited to 3 characters only
    while len(game_id) != 3:
        print("Enter your name ( 3 characters only )")
        game_id = input("")
    
    return game_id



def list_of_items(items):
    """This function takes a list of items (see items.py for the definition) and
    returns a comma-separated list of item names (as a string). For example:

    >>> list_of_items([item_pen, item_handbook])
    'a pen, a student handbook'

    >>> list_of_items([item_id])
    'id card'

    >>> list_of_items([])
    ''

    >>> list_of_items([item_money, item_handbook, item_laptop])
    'money, a student handbook, laptop'

    """

    # Add each item name to the string with a comma and space.
    item_list = ""
    for item in items:
        item_list += str(item["name"] + ", ")

    # Remove the final comma+space pair and return string.
    return item_list[:-2]


def print_room_items(room):
    """This function takes a room as an input and nicely displays a list of items
    found in this room (followed by a blank line). If there are no items in
    the room, nothing is printed. See map.py for the definition of a room, and
    items.py for the definition of an item. This function uses list_of_items()
    to produce a comma-separated list of item names. For example:

    >>> print_room_items(rooms["Reception"])
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room_items(rooms["Office"])
    There is a pen here.
    <BLANKLINE>

    >>> print_room_items(rooms["Admins"])

    (no output)

    Note: <BLANKLINE> here means that doctest should expect a blank line.

    """

    item_list = list_of_items(room["items"])
    if item_list:
        print(str("There is " + item_list + " here.\n"))
        

def print_inventory_items(items):
    """This function takes a list of inventory items and displays it nicely, in a
    manner similar to print_room_items(). The only difference is in formatting:
    print "You have ..." instead of "There is ... here.". For example:

    >>> print_inventory_items(inventory)
    You have id card, laptop, money.
    <BLANKLINE>

    """

    item_list = list_of_items(items)
    if item_list:
        print(str("You have " + item_list + ".\n"))


def print_room(room):
    """This function takes a room as an input and nicely displays its name
    and description. The room argument is a dictionary with entries "name",
    "description" etc. (see map.py for the definition). The name of the room
    is printed in all capitals and framed by blank lines. Then follows the
    description of the room and a blank line again. If there are any items
    in the room, the list of items is printed next followed by a blank line
    (use print_room_items() for this). For example:

    >>> print_room(rooms["Office"])
    <BLANKLINE>
    THE GENERAL OFFICE
    <BLANKLINE>
    You are standing next to the cashier's till at
    30-36 Newport Road. The cashier looks at you with hope
    in their eyes. If you go west you can return to the
    Queen's Buildings.
    <BLANKLINE>
    There is a pen here.
    <BLANKLINE>

    >>> print_room(rooms["Reception"])
    <BLANKLINE>
    RECEPTION
    <BLANKLINE>
    You are in a maze of twisty little passages, all alike.
    Next to you is the School of Computer Science and
    Informatics reception. The receptionist, Matt Strangis,
    seems to be playing an old school text-based adventure
    game on his computer. There are corridors leading to the
    south and east. The exit is to the west.
    <BLANKLINE>
    There is a pack of biscuits, a student handbook here.
    <BLANKLINE>

    >>> print_room(rooms["Admins"])
    <BLANKLINE>
    MJ AND SIMON'S ROOM
    <BLANKLINE>
    You are leaning agains the door of the systems managers'
    room. Inside you notice Matt "MJ" John and Simon Jones. They
    ignore you. To the north is the reception.
    <BLANKLINE>

    Note: <BLANKLINE> here means that doctest should expect a blank line.
    """
  
    # Display room name
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    if room["items"]:
        print_room_items(room)
        

def exit_leads_to(exits, direction):
    """This function takes a dictionary of exits and a direction (a particular
    exit taken from this dictionary). It returns the name of the room into which
    this exit leads. For example:

    >>> exit_leads_to(rooms["Reception"]["exits"], "south")
    "MJ and Simon's room"
    >>> exit_leads_to(rooms["Reception"]["exits"], "east")
    "your personal tutor's office"
    >>> exit_leads_to(rooms["Tutor"]["exits"], "west")
    'Reception'
    """
    return rooms[exits[direction][0]]["name"]


def print_exit(direction, leads_to):
    """This function prints a line of a menu of exits. It takes a direction (the
    name of an exit) and the name of the room into which it leads (leads_to),
    and should print a menu line in the following format:

    GO <EXIT NAME UPPERCASE> to <where it leads>.

    For example:
    >>> print_exit("east", "you personal tutor's office")
    GO EAST to you personal tutor's office.
    >>> print_exit("south", "MJ and Simon's room")
    GO SOUTH to MJ and Simon's room.
    """
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    """This function displays the menu of available actions to the player. The
    argument exits is a dictionary of exits as exemplified in map.py. The
    arguments room_items and inv_items are the items lying around in the room
    and carried by the player respectively. The menu should, for each exit,
    call the function print_exit() to print the information about each exit in
    the appropriate format. The room into which an exit leads is obtained
    using the function exit_leads_to(). Then, it should print a list of commands
    related to items: for each item in the room print

    "TAKE <ITEM ID> to take <item name>."

    and for each item in the inventory print

    "DROP <ITEM ID> to drop <item name>."

    For example, the menu of actions available at the Reception may look like this:

    You can:
    GO EAST to your personal tutor's office.
    GO WEST to the parking lot.
    GO SOUTH to MJ and Simon's room.
    TAKE BISCUITS to take a pack of biscuits.
    TAKE HANDBOOK to take a student handbook.
    DROP ID to drop your id card.
    DROP LAPTOP to drop your laptop.
    DROP MONEY to drop your money.
    What do you want to do?

    """
    #Now gives the player a template for any item in the current room or their inventory
    #instead of looping the same command for each item - avoids clutter on screen.
    
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    # Iterate over available items
    print("TAKE [item] to pick up an item")

    # Iterate through inventory
    print("DROP [item] to drop an item")

    #gives the player additional information on items in their inventory or in the current room
    print("INSPECT [item] to find out more about an item")
    
    print("What do you want to do?")
    print("="*100)


def is_valid_exit(exits, chosen_exit):
    """This function checks, given a dictionary "exits" (see map.py) and
    a players's choice "chosen_exit" whether the player has chosen a valid exit.
    It returns True if the exit is valid, and False otherwise. Assume that
    the name of the exit has been normalised by the function normalise_input().
    For example:

    >>> is_valid_exit(rooms["Reception"]["exits"], "south")
    True
    >>> is_valid_exit(rooms["Reception"]["exits"], "up")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "west")
    False
    >>> is_valid_exit(rooms["Parking"]["exits"], "east")
    True
    """
    return chosen_exit in exits

def is_valid_mass(inv_items):
    weight = 0
    
    for masses in inventory:
        weight = weight + masses["mass"]

    return(weight)


def menu_gate(key, direction):
    #interaction with the child gate. starts its own loop until the correct passwordis inputted
    global current_room
    while True:
        user_input = input("Enter the password for the gate to unlock it, or type BACK to go back.\n> ")
        user_input = normalise_input(user_input)[0]
        print(key)
        if user_input == "back":
            return
        elif user_input == key:
            # Leave this exit unlocked
            current_room["exits"][direction][1] = False
            current_room = rooms[current_room["exits"][direction][0]]
            return


def menu_item(key, direction):
    #interaction with locked doors which require a key. starts its own loop until the correct item is used.
    global current_room
    while True:
        user_input = input("The exit is shut!\nChoose an item to use on it or type BACK to go back.\n> ")
        user_input = normalise_input(user_input)[0]
        #print(user_input)
        if user_input == "back":
            return
        else:
            for item in inventory:
                if item["id"] == user_input:
                    print(str("You used " + item["name"]))
                    if user_input == key["id"]:
                        print("The door opened.")
                        current_room["exits"][direction][1] = False
                        current_room = rooms[current_room["exits"][direction][0]]
                        return
                    else:
                        print("That didn't work.")


def prompt_unlock(key, direction):
    #changes the boolean value of the exit
    global current_room
    if isinstance(key, str):
        menu_gate(key, direction)
    elif isinstance(key, bool):
        if key:
            current_room["exits"][direction][1] = False
            current_room = rooms[current_room["exits"][direction][0]]
        else:
            print("The door is so dirty it won't open.")
    else:
        menu_item(key, direction)


def execute_go(direction):
    """This function, given the direction (e.g. "south") updates the current room
    to reflect the movement of the player if the direction is a valid exit
    (and prints the name of the room into which the player is
    moving). Otherwise, it prints "You cannot go there."
    """
    global current_room
    try:
        check = current_room["exits"][direction][1]
    except KeyError:
        print("You cannot go that way!")
        return
    if current_room["exits"][direction][1]:
        # Exit is locked
        prompt_unlock(current_room["exits"][direction][2], direction)
    else:
        # Exit is unlocked
        current_room = rooms[current_room["exits"][direction][0]]
        

def execute_take(item_id):
    """This function takes an item_id as an argument and moves this item from the
    list of items in the current room to the player's inventory. However, if
    there is no such item in the room, this function prints
    "You cannot take that."
    """

    for item in current_room["items"]:
        if item["id"] == item_id and item["can_take"]:
            if is_valid_mass(inventory) + item["mass"] <= 2.0:
                current_room["items"].remove(item)
                inventory.append(item)
                if is_valid_mass(inventory) >= 1.5:
                    print("Current weight = " + str(is_valid_mass(inventory)) + "kg")
                    print("MAX carry capacity = 2.0kg")
                return
            
    print("You cannot take that.")
    

def execute_drop(item_id):
    """This function takes an item_id as an argument and moves this item from the
    player's inventory to list of items in the current room. However, if there is
    no such item in the inventory, this function prints "You cannot drop that."
    """

    for item in inventory:
        if item["id"] == item_id:
            inventory.remove(item)
            current_room["items"].append(item)
            return
    print("You cannot drop that.")

    
def execute_inspect(item_id):
    #gives the player additional information on items in their inventory or in the current room
    for names in current_room["items"]:
        if names["id"] == item_id:
            print(names["description"])
            if names["can_take"]:
             print("item mass = " + str(names["mass"]) + "kg")
            return
        
    for names in inventory:
        if names["id"] == item_id:
            print(names["description"])
            if names["can_take"]:
                print("item mass = " + str(names["mass"]) + "kg")
            return

            
def execute_clean(item):
    #allows the player to use items to clean rooms or other items
    if item_mop in inventory and item_soap in inventory:
        if item == "bathroom":
            if current_room["name"] == "Bathroom":
                print("The bathroom is now spotless!")
                rooms["Bathroom"]["description"] = """You are now in a shiny clean bathroom. There is a sign on the wall above the sink.
Go west to re-enter the bedroom. The exit to the south is an exit into the corridor."""
                current_room["exits"]["south"][2] = True
            else:
                print("You're not in that room!")
        elif item == "plates":
            if item_plates in inventory or item_plates in current_room["items"]:
                item_plates["description"] = "Some shiny plates"
                rooms["Kitchen"]["description"] = """You are now in a kitchen. You can
go east to return to the hallway. The exit to the south leads to a dining room
and is currently jammed."""
                print("The plates are now hygienic.")
                
        else:
            print("You cannot clean that.")
    else:
        print("You need 2 cleaning products to do this!")



def execute_command(command):
    """This function takes a command (a list of words as returned by
    normalise_input) and, depending on the type of action (the first word of
    the command: "go", "take", or "drop"), executes either execute_go,
    execute_take, or execute_drop, supplying the second word as the argument.

    """
    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")

    elif command[0] == "clean":
        if len(command) > 1:
            execute_clean(command[1])
        else:
            print("Clean what?")

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):
    """This function, given a dictionary of possible exits from a room, and a list
    of items found in the room and carried by the player, prints the menu of
    actions using print_menu() function. It then prompts the player to type an
    action. The players's input is normalised using the normalise_input()
    function before being returned.

    """
    
    # Display menu
    if current_room["name"] == "Exit":
        return "complete"
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    """This function returns the room into which the player will move if, from a
    dictionary "exits" of avaiable exits, they choose to move towards the exit
    with the name given by "direction". For example:

    >>> move(rooms["Reception"]["exits"], "south") == rooms["Admins"]
    True
    >>> move(rooms["Reception"]["exits"], "east") == rooms["Tutor"]
    Trues
    >>> move(rooms["Reception"]["exits"], "west") == rooms["Office"]
    False
    """

    # Next room to go to
    return rooms[exits[direction]]


def finish(score):
    print(str("You FINISHED in " + str(score) + "seconds"))
    #while True:
        #input()

# This is the entry point of our program
def main():

    global game_id
    
    #starts a timer which is used for the player's score

    start_menu()
    start = time.time()

    # Main game loop
    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        if command != "complete":
            # Execute the player's command
            execute_command(command)
        else:
            # Calculating the player's time
            end = time.time()
            player_score = round(end - start)
            finish(player_score)
            break

    # Display scoreboard at the end of the game
    get_scores(game_id, player_score)



# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

