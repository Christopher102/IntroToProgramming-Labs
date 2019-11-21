# This is a small program that allows players to have a simple score interface.
# The player progresses through various locations by hitting enter


def game():
    playerlocation = ['Location1', 'Location2', 'Location3', 'Location4', 
                      'Location5']
    print('\n'*100)
    print('''Farlandia''')
    print('''You wake up in the middle of a dark forest, with nobody around.
Trees strech into the sky around you, and theres a path beneath your feet that
leads into the darkness. You decide to follow it out of the forest.''')
    playerscore = 0
    print('\n'*10)
    print(playerlocation[0])
    print(playerscore)
    input("Press Enter to Continue")
    print('\n'*100)
    print('''You arrive outside the woods into a sunny field. The road forks,
    both destinations not within your sight. One direction says "Fort, the
    other says "Town". Unsure of how far either are,
    you decide to go to the fort.''')
    playerscore += 5
    print('\n'*10)
    print(playerlocation[1])
    print(playerscore)
    input("Press Enter to Continue")
    print('\n'*100)
    print('''Upon arriving at the fort, arrows are fired at you. You dodge,
    then hold your hands up in mock surrender. A guard calls over, asking who
    you are. You don't have an answer, so he turns you away with another
    volley of arrow fire.''')
    playerscore += 5
    print('\n'*10)
    print(playerlocation[2])
    print(playerscore)
    input("Press Enter to Continue")
    print('\n'*100)
    print('''You leave the fort and go back to the fork in the road.
    When you arrive, a caravan is under seige by bandits.
    You quickly grab a weapon from one of the fallen, jumping into the fray.
    They are defeated quickly, and the caravan thanks you for your assistance
    and asks you to join them. You accept.''')
    playerscore += 5
    print('\n'*10)
    print(playerlocation[3])
    print(playerscore)
    input("Press Enter to Continue")
    print('\n'*100)
    print('''You travel with the caravan for a number of weeks before
arriving at the town. You get off your horse, happy to finally be in a
stable place once more. You and your new caravan friends
make your way to the tavern. ''')
    playerscore += 5
    print('\n'*10)
    print(playerlocation[4])
    print(playerscore)
    input("Press Enter to Continue")
    print('\n'*100)
    print('''You and your new friends spend the night drinking,
and the leader of the caravan approaches you. He offers you
a permanent position with the caravan, and you happily accept.
The next morning,
you and your party leave in search of the next adventure.''')
    print("Congratulations! You've Won!")
    print(" ")
    print("Final score: ", playerscore)
    print('\n'*10)
    print("Copywrite by Chris Fioti and John Goll")
    print("Emails: Christopher.Fioti1@marist.edu, John.Goll1@marist.edu")


game()


