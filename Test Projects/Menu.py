# testing out a main menu with options in python
import math
import time


class color:
    blue = '\033[94m'
    underline = '\033[4m'
    purple = '\033[95m'
    end = '\033[0m'
    red = '\033[91m'


def death():
    print("\n"*100)
    print("You have perished!")
    print("Please try again.")
    print("You final score was: ")
    print(color.purple + playerscore + color.end)


def win():
    print(color.purple + "Congratulations!")
    print("You've beaten my game!")
    print("Your final score was: " + playerscore)
    print("Please play again!" + color.end)


def menu():
    print('\n'*75)
    print(30 * "-", "MENU", 30 * "-")
    print("1. Play")
    print("2. Options")
    print("3. Exit")
    print(67 * "-")


loop = True


def Hellfire_Ship():
    print('\n'*100)
    print("Once inside, you take a look around the cockpit.")
    print("It's a mess of buttons and wires")
    print("You sit in the captains chair, feeling more powerful then ever.")
    print("You look at the console and are immediately overwhelmed.")
    print("You decide two buttons are important: Red and Green")
    choice5 = int(input("Which do you press? 1. Red or 2. Green?"))
    if choice5 == 1:
        playerscore = 25
        print('\n'*100)
        print(color.blue + "You slam your first down on the red button")
        print("The ship begins to shudder and shake...")
        print("The ship suddenly shoots upward, pressing you into your seat.")
        print("As you fly, you look at the stars above")
        print("You smile as the voice in your head speaks one more time." + color.end)
        print("Congratulations {}, you survived. I'll send you some other place soon.".format(name))
        win()


def Hellfire_Outside():
    print(color.blue + "The outside is even hotter than the inside")
    print("You are standing on the edge of a castle, looking out upon the fields.")
    print("Fields of fire, I mean.")
    print("Literally. Everything is on fire. Including the fire")
    print("Gleaming blue against the flames, shines a spaceship.")
    print("It's your ticket out of here")
    print("You run towards it, hoping theres no pilot.")
    print("Down the stairs and over the only safe path, you eventually stumble upon it")
    print("After patting out the fire on your legs, you stare at the marvelous ship" + color.end)
    choice4 = int(input("Do you 1. Get in the ship or 2. Stare a bit more"))
    if choice4 == 1:
        print("You walk towards the ship, it's bay doors already open for you.")
        Hellfire_Ship()


def Hellfire_dungeon():
    time.sleep(5)
    print("\n"*100)
    print(color.blue + "YOU ARE TELEPORTED TO A DUNGEON CELL.")
    print("IT IS BOILING HOT INSIDE, THE WALLS ARE MADE OF DARK BASALT")
    print("AND THE BARS ARE MADE OF THE BLACKEST OBSIDIAN IMAGINABLE")
    print("THERE APPEARS TO BE A LOOSE BRICK IN THE WALL")
    print("HOWEVER, ONE OF THE BARS IS LOOSE ON THE GATE" + color.end)
    choice3 = int(input("DO YOU 1. TRY THE BRICK OR 2. TRY THE BAR >"))
    if choice3 == 1:
        print("\n")
        print(color.blue + "The brick comes loose! You manage to peer outside")
        print("You see bandits, all standing around blue flames")
        print("You begin to quietly pull down other bricks")
        print("The hole is now big enough for you to crawl through")
        print("You crawl through and begin to make your way around the bandits" + color.end)
        choicebrick = int(input("Do you 1. Be as quiet as possible or 2. Attempt to fight?"))
        if choicebrick == 1:
            print(color.blue + "You quietly sneak past the bandits")
            print("You make your way to the door on the far side, and slip through" + color.end)
            Hellfire_Outside()
        elif choicebrick == 2:
            print("You get up and get the bandits attention.")
            print("You don't have a weapon")
            print("They rush you")
            death()

    elif choice == 2:
        print(color.blue + "You pry the bar off. You now have a sharp rod.")
        print("You step through the bars and are immediately met with a sword")
        print("You dodge, and turn to see a rather large bandit" + color.end)
        print(color.red + "WHAT DO YOU THINK YOU'RE DOING?")
        print("YOU AREN'T LEAVING ALIVE!" + color.end)
        print(color.blue + "He charges at you, blade swinging." + color.end)
        choicebar = int(input("1. Block the swing 2. Try to go for a stab? "))
        if choicebar == 1:
            print("You hold up the bar to block his hit")
            print("Unfortunately, you aren't nearly as strong as him.")
            print("The swing of his blade takes the bar (And your head) off.")
            death()
        elif choicebar == 2:
            print("You thrust forward just as he raises his sword")
            print("The sharp end of the bar goes straight through his heart")
            print("He falls over, and bleeds out. You take his sword.")


def Start_game():
    print('\n'*75)

    print("Welcome to Wonderland!")
    print("Before we begin, I must ask you a couple of questions.")
    print()
    name = input("Tell me, whats your name? > ")
    print('\n'*75)
    print("Well then {}, let be the first to tell you.".format(name))
    print()
    print("This place? It sucks.")
    print()
    print("If you wanna get out, you gotta fight. So tell me this...")
    choice2 = input("Are you 1. Brave? or 2. Smart? >")
    choice2 = int(choice2)
    print('\n'*75)
    if choice2 == 1:
        print("Then you've won a one way ticket to Hellfire-9.")
        print()
        print("The doom planet!")
        print()
        print("So, here's the deal muchacho.")
        print()
        print("Hellfire-9 is, as it sounds, really hot")
        print("In addition to that...")
        print("BANDITS. A whole lot of 'em")
        print()
        print("So your job is to escape. Sounds pretty simple...")
        print(color.red + "In fact, it's too simple." + color.end)
        Hellfire_dungeon()

    elif choice2 == 2:
        print("Then you'll love the swamp lands of Marsh-6.")
        time.sleep(1)
        print()
        print("Home of the swamp bugs!")


def options_menu():
    print("Listen man, did you really expect options in a text-based")
    print("adventure game? Good. Cause I didn't come up with any")
    exit()


while loop:
    menu()
    choice = input("Enter 1-3 to make a selection >")
    choice = int(choice)
    if choice == 1:
        print("Starting game...")
        Start_game()

    elif choice == 2:
        print("Opening options...")
        options_menu()

    elif choice == 3:
        print("Exiting...")
        exit()

    else:
        print("Wrong Selection. Please choose 1-3.")

    loop = False
