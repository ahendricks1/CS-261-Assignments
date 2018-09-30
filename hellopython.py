'''
-Need five areas with at least five to eight interactable items
-Start in room with door, window, and cabinet(locked)
-Can exit through door or window to new area
-If door is chosen, enter larger room with two more doors, one west, one north again.
    If west door is chosen, user is killed
    If north door is chosen, come to a dark room with light switch and key on a table for the cabinet in starting room
-If key is used on cabinet receive a flashlight
-If window is chosen, you enter a yard with a shed
-If you go into the shed without a flaslight, you are killed
-Once you enter shed with flashlight, you can find a tunnel you may enter and escape alive!

-Print the current location name + description
-Wait for user to type a command
-Parse the user command
-Response to the command
-Return to the start
'''

# Room blueprint
class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.item = None

# Map title and description
windowRoom = Room("Chilly Side Yard", "After crawling through the window you find yourself in a dark yard, the only thing in sight is a shed with no lights on inside.")
northHallway = Room("Dim Hallway", "The door creaks open, revealing a dim hallway with another door to the north as well as one to the west.")
northRoom = Room("Pitch Black Room", "Carefully peering inside reveals...nothing at all? The lights are off silly!")
westRoom = Room("Your Unfortunate Demise", "Before your hand makes contact with the knob, the door whips open, and you are dragged into utter darkness. Sorry!")
shedRoom = Room("Seemingly Average Shed", "Upon entering the shed, you are met with a surprsingly large hole that has seemingly been ripped out of the back side of the shed, which leads out to the main street, where you can see other people walking around. You're free!")
startRoom = Room("Lowlight Spooky Room", "You are in a dark room, to the north there is a door, to the east there is a window, and there is a cabinet across from you.")

# Map layout
startRoom.north = northHallway
startRoom.east = windowRoom
northHallway.north = northRoom
northHallway.south = startRoom
northHallway.west = westRoom
northRoom.south = northHallway
windowRoom.north = shedRoom
windowRoom.south = shedRoom
windowRoom.west = startRoom
windowRoom.east = shedRoom

# Starting position, default room, and default inventory
currentRoom = startRoom
inventory = []
print(startRoom.title)
print(startRoom.description)

# Directional loop for rooms and inventory items
while(True):
    if currentRoom == westRoom:
        restart = input("Play again? Y or N? ")
        restart = restart.lower()
        if restart == "n":
            exit()
        else:
            currentRoom = startRoom
            inventory = []
            print(startRoom.title)
            print(startRoom.description)
            continue
    else:
        choice = input("What do you do? ")
        choice = choice.lower()
        if choice == "north":
            if currentRoom.north == None:
                print("You cannot go that direction!")
            else:
                currentRoom = currentRoom.north
                print(currentRoom.title)
                print(currentRoom.description)
        elif choice == "south":
            if currentRoom.south == None:
                print("You cannot go that direction!")
            else:
                currentRoom = currentRoom.south
                print(currentRoom.title)
                print(currentRoom.description)
        elif choice == "east":
            if currentRoom.east == None:
                print("You cannot go that direction!")
            else:
                currentRoom = currentRoom.east
                print(currentRoom.title)
                print(currentRoom.description)
        elif choice == "west":
            if currentRoom.west == None:
                print("You cannot go that direction!")
            else:
                currentRoom = currentRoom.west
                print(currentRoom.title)
                print(currentRoom.description)
        elif choice == "key" or "cabinet" or "light":
            if choice == "cabinet":
                if "key" in inventory:
                    print("You find...a flashlight? You might as well take it too.")
                    inventory.append("flashlight")
                else:
                    print("It's locked you dingus!")
            elif choice == "light":
                print("The light flashes on, and you see an old copper key on the table next to you...and not much else.")
            elif choice == "key":
                print("You put the key in your pocket you smarty pants.")
                inventory.append("key")
        else:
            print("That is not possible you goober.")


'''
def north():
    return

def south():
    return

def east():
    return

def west():
    return

def look():
    return

def restart():
    return

def quit():
    if userInput == 'quit':
        exit()
    return

def use():
    return

def userInput():
    input()
    return
'''