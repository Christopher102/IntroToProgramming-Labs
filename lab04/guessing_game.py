# This game has the player guessing what animal I, the program, am thinking of.

# These two are used for my "time stops" and random animal generator
import random
import time

# This defines the "mouse" path


def mouse():
    print("\n"*100)
    print("What is used with a keyboard for a computer?")
    guess = input("What is the answer? -> ")
    guess = guess.lower()
    if guess == "mouse":
        print("Congratulations! You've Guessed it!")
        print("My animal was a Mouse!")
    elif guess[:1] == "q":  # Defines the "Exit"
        return None
    else:
        print("\n"*10)
        print("I'm sorry! That was not my animal! Please try again!")
        time.sleep(3)
        mouse()
# This defines the "phoenix" path


def phoenix():
    print("\n"*100)
    print("This animal bursts into flames and is reborn from it's own ashes.")
    guess = input("What is this animal? -> ")
    guess = guess.lower()
    if guess == "phoenix":
        print("Congratulations! You've Guessed it!")
        print("My animal was a Phoenix!")
    elif guess[:1] == "q":
        return None
    else:
        print("\n"*10)
        print("I'm sorry! That was not my animal! Please try again!")
        time.sleep(3)
        phoenix()

# This defines the "Cat" path, where the computer has selected "Cat"


def cat():
    print("\n"*100)
    print("I hunt mice and are considered an old lady's pastime. What am I?")
    guess = input("What is your guess? -> ")
    guess = guess.lower()
    if guess == "cat":
        print("Congratulations! You've Guessed it!")
        print("My animal was a Cat!")
    elif guess[:1] == "q":
        return None
    else:
        print("\n"*10)
        print("I'm sorry! That was not my animal! Please try again!")
        time.sleep(3)
        cat()

# This defines the "Tiger" path, where the computer has selected it's word
# To be "Tiger"


def tiger():
    print("\n"*100)
    print("What animal has stripes, walks on four legs, and is orange?")
    guess = input("What is your guess? -> ")
    guess = guess.lower()
    if guess == "tiger":
        print("Congratulations! You've Guessed it!")
        print("My animal was a Tiger!")
    elif guess[:1] == "q":
        return None
    else:
        print("\n"*10)
        print("I'm sorry! That was not my animal! Please try again!")
        time.sleep(3)
        tiger()

# This defines the "Dog" path, where the computer selects "Dog"


def dog():
    print("\n"*100)
    print("I am mans best friend. Who am I?")
    guess = input("What is your guess? -> ")
    guess = guess.lower()
    if guess == "dog":
        print("Congratulations! You've Guessed it!")
        print("My animal was a Dog!")
    elif guess[:1] == "q":
        return None
    else:
        print("\n"*10)
        print("I'm sorry! That was not my animal! Please try again!")
        time.sleep(3)
        dog()

# This defines the "Donkey" path, where the computer selects "Donkey"


def donkey():
    print("\n"*100)
    print("The animal I am thinking of can be guessed by solving this riddle:")
    print("What kind of key is the hardest to turn?")
    guess = input("What is the answer? -> ")
    guess = guess.lower()
    if guess == "donkey":
        print("Congratulations! You've Guessed it!")
        print("My animal was a Donkey!")
    elif guess[:1] == "q":
        return None
    else:
        print("\n"*10)
        print("I'm sorry! That was not my animal! Please try again!")
        time.sleep(3)
        donkey()

# This is the function that selects an animal for the player to guess


def game():
    animal1 = "Donkey"
    animal2 = "Tiger"
    animal3 = "Dog"
    animal4 = "Cat"
    animal5 = "Mouse"
    animal6 = "Phoenix"
    animals = [animal1, animal2, animal3, animal4, animal5, animal6]
    animals = random.choice(animals)
    print(animals)
    if animals == animal1:
        donkey()
    elif animals == animal2:
        tiger()
    elif animals == animal3:
        dog()
    elif animals == animal4:
        cat()
    elif animals == animal5:
        mouse()
    elif animals == animal6:
        phoenix()


game()
