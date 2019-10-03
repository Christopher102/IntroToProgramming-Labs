# CMPT 120 Intro to Programming
# Lab 5 - WOrking with Strings and Functions
# Author: Chris Fioti
# Created: 2019-10-03


def main():
    # get the user's first and last names
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    uname = first + "." + last + "1"
    passwrd = input("Create a new password: ")
    while len(passwrd) < 8:
        print("Fool of a took! That password is feeble!")
        print('\n')
        passwrd = input("Create a New Password: ")
    else:
        print('\n')
        print("The Force Is Strong with This One")
    print("Account Created. Your new email is " + uname + "@marist.edu")


main()
