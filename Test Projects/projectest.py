# This is the first part of the semester project
# It is a text-based adventure game, version 0.1

import time


class color:
    blue = '\033[94m'
    underline = '\033[4m'
    purple = '\033[95m'
    end = '\033[0m'
    red = '\033[91m'


playerscore = 0
playerlocation = 0


def game():
    print('\n'*50)
    print("Hello, and welcome to Farlandia!")
    playerscore = 0
    player_location = 0
    print('''A land full of magical and mystical things!
You're currently lost in a dark forest, with dangerous creatures all around.
There is a path beneath your feet, however you can't see where it's going.
You could climb to get a better view, but the trees are 100 feet tall''')
    print('\n'*10)
    print("Current Score:", playerscore)
    print("Current Location: Dark Forest")
    print("Which do you do?:")
    print()
    choice1 = int(input("1. Follow the path or 2. Climb a tree? "))
    if choice1 == 2:
        print('\n'*100)
        print('''You climb the tree.
Unfortunately, you aren't as good of a climber as you thought.
You get halfway up, then fall to your death.''')
        time.sleep(5)
        print("\n"*100)
        print("You lose!")
        print("Please try again.")
        print("Final Score: {}".format(playerscore))
    elif choice1 == 1:
        playerscore = 5
        player_location = 1
        print('\n'*100)
        print('''You begin to head down the path into the darkness.
As you walk, you hear what sounds like voices echoing through the trees.
Suddenly, you hear a sharp hiss.
A SNAKE! Pitch black with bright red eyes. It's about to lunge
But, the exit. You can see it, just beyond the snake.''')
        print('\n'*10)
        print("Current Score:", playerscore)
        print("Current Location: Dark Forest")
        print()
        choice2 = int(input("Do you 1. Run or 2. Fight? "))
        if choice2 == 1:
            print('\n'*100)
            print('''You turn to run, but the snake is faster
It bites you, wraps itself around you.
Your last thoughts are of whether or not you taste good.''')
            time.sleep(5)
            print('\n'*100)
            print("You lose!")
            print("Please try again!")
            print("Final Score: {}".format(playerscore))
        elif choice2 == 2:
            print('\n'*100)
            print("The snake lunges!")
            print('''You dodge, grab it by the tail,
and swing it into the nearest tree. It dies on impact.
Breathless and feeling stronger, you make your way out of the forest.''')
            player_location = 1
            playerscore = 10
            time.sleep(6)
            print('\n'*100)
            print("You step out unto the bright plains.")
            print('''You hold your hand up to shield from the sun, it's rays
burning into your retinas as they adjust. Ahead, you can see the path splits.
You walk over to the fork, and look at the signs.
One says "Town"
The other, "Fort"
Which do you chose?''')
            print("\n"*10)
            print("Current Score:", playerscore)
            print("Current Location: Sunny Field Fork")
            choice3 = int(input("1. Town or 2. Fort? "))
            if choice3 == 1:
                print('\n'*100)
                print('''You begin to meander down the road towards the town
And the road keeps going
And going
And going
And going
...''')
                time.sleep(10)
                print('''Maybe next time you should check how far it is.
You die long before ever reaching the town''')
                time.sleep(5)
                print("\n"*100)
                print("You lose!")
                print("Please try again!")
                print("Final Score: {}".format(playerscore))
            elif choice3 == 2:
                player_location = 2
                playerscore = 15
                print('\n'*100)
                print('''You walk slowly towards the fort,
wary of dangers on the road.
After an hour's walk, you arrive.
It is situated on top of a nearby hilltop, helping to make it's
defenses even more impenetrable. It is made of dark grey stone,
the parapets and towers gleaming in the sunlight. As you approach, you
can hear sounds of guards and soldiers training in the courtyard.
A voice calls out to you.''')
                print(color.blue + '''Who goes there?
State your business or be killed!''' + color.end)
                print("Do you tell him the truth? Or lie to gain access?")
                print('\n'*10)
                print("Current Score: ", playerscore)
                print("Current Location: Fort Obystyre")
                choice4 = int(input("1. The Truth or 2. Lie "))
                if choice4 == 2:
                    print('\n'*100)
                    print('''You tell him you're a soldier,
lost from a nearby battleground.''')
                    print(color.blue + '''Oh, alright, I'll let you in!"
                    ''' + color.end)
                    print("You wait for him to open the gates.")
                    print("...")
                    time.sleep(5)
                    print('''An arrow, from one of the murder holes, shoots out
and pierces straight through your heart.
Honesty is the best policy, as they always say.''')
                    time.sleep(5)
                    print("\n"*100)
                    print("You lose!")
                    print("Please try again!")
                    print("Final Score: {}".format(playerscore))
                if choice4 == 1:
                    print('\n'*100)
                    print(color.blue + '''Oh that seems very reasonable.
We get lost all the time. Come in!''' + color.end)
                    print('''The doors to the fort swing wide open,
and you step inside. Within, there is a big courtyard,
filled with training dummies and other training equipment.
Some is in use, some not.
The speaker from before comes down to greet you.''')
                    print(color.blue + '''Hey there.
Listen, tell me your name so we can chat a bit.''' + color.end)
                    playername = input("What is your name?: ")
                    print('\n'*100)
                    print(color.blue + '''Well, {} I'm here to help you.
You looked destroyed.'''.format(playername))
                    print('''Here's a guards outfit and a sword.
Now, get lost before my boss shows up.''' + color.end)
                    time.sleep(10)
                    print('\n'*100)
                    print('''You gratefully accept the outfit,
happy to be out of your worn drabs.
The outfit is emblazoned with a green lion and is made of a velvet material
You put it on, and begin to feel more refreshed than before.
After thanking the guard, you make your way back down the road.
A caravan has stopped at the fork in the road.''')
                    player_location = 1
                    playerscore = 20
                    print("As you approach, you hear people shouting.")
                    print(color.red +
                          '''This is why I said we needed guards!'''
                          + color.end)
                    print(color.purple +
                          '''Well I thought the forest was empty!'''
                          + color.end)
                    print(color.red +
                          '''Well now we need a guard,
cause our weapons guy is dead!''' + color.end)
                    print('''They notice you, and call you over.
They say they are a caravan from a town across the forest.
They were coming to trade with the other town, and need some protection.''')
                    print('\n'*10)
                    print("Current Score: ", playerscore)
                    print("Current Location: Sunny Field.")
                    print("Do you help them?")
                    choice5 = int(input("1. Yes? or 2. No? "))
                    if choice5 == 2:
                        print('\n'*100)
                        print('''You choose against helping them,
and continue on your way to the town
However, you still forgot that you have no food or water.
You die long before you reach the town.''')
                        time.sleep(5)
                        print("You Lose!")
                        print("Please Try Again!")
                        print("Final Score: {}".format(playerscore))
                    elif choice5 == 1:
                        print('\n'*100)
                        print('''You agree to help them in their venture.
They look relieved.
You saddle up one of their horses and travel with them.''')
                        time.sleep(5)
                        print("\n"*100)
                        print("A few days pass by...")
                        time.sleep(2)
                        print('''You arrive in the town,
with no harm having come to the caravan.''')
                        player_location = 3
                        playerscore = 25
                        print('''After travelling with the caravan,
you decide to stay with them, travelling along.
You stop in the tavern to celebrate your arrive and to have a drink.
The inside is musky, laden with the smell of booze and cheap games of cards.
You sit down with your new friends, laughing and celebrating.
Congratulations, you've won.''')
                        time.sleep(10)
                        print("\n"*100)
                        print("Congratulations, you've beaten my game!")
                        print("Thanks for playing!")
                        print("Final Score: ", playerscore)
                        print('''Copyright Chris Fioti,
                        Christopher.Fioti@Marist.edu''')


game()
