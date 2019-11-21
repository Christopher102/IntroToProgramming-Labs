# Fill in the blanks Mad Libs Game
# Enter in 4 words and it'll make a sentence!


def main():
    phrases = []
    count = 0
    while count != 4:
        noun = input("Please enter a noun >")
        verb = input("Please enter a verb >")
        adjective = input("Please enter an adjective >")
        place = input("Please enter a location >")
        phrase = noun, verb, "to the", adjective, place
        phrases.append(phrase)
        count += 1
    print(phrases, end="\n")


main()
