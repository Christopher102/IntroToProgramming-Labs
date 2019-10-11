# CMPT 120 Intro to Programming
# Lab 5 - Working with Strings and Functions
# Author: Chris Fioti
# Created: 2019-10-03

import re
unames = []
upasswords = []


def names():
    first = input("Please enter your first name: ").lower()
    last = input("Please enter your last name: ").lower()
    fullname = [first, last]
    return fullname


def user(fullname):
    userN = str(fullname[0] + "." + fullname[1])
    userN += str(len([name for name in unames if name.startswith(userN)]) + 1)
    unames.append(userN)
    return userN


def password():
    passwd = input("Create a new password: ")
    return passwd


def passwordcheck(passwd):
    length_error = len(passwd) < 8
    digitcheck = re.search("[0-9]", passwd) is None
    Uppercheck = re.search("[A-Z]", passwd) is None
    Lowercheck = re.search("[a-z]", passwd) is None
    password_ok = not (length_error or digitcheck or Uppercheck or Lowercheck)
    if password_ok is False:
        print("Fool of a took! That password is feeble!")
        if length_error is True:
            print("Password is not long enough")
        elif digitcheck is True:
            print("Password must have numbers")
        elif Uppercheck is True:
            print("Password must have uppercase numbers")
        elif Lowercheck is True:
            print("Password must have lowercase numbers")
        return passwordcheck(password())
    else:
        print("This force is strong with this one!")
        return passwd


def main():
    loop = True
    namecounter = 0
    while loop is True:
        Username = str(user(names()))
        passfinal = passwordcheck(password())
        print("Account Created. Your new email is " + Username + "@marist.edu")
        namecounter += 1
        print("There are currently {} usernames".format(namecounter))
        upasswords.append(passfinal)
        restart = input("Input another name? (Y/N): ")
        if restart.lower() == "y":
            loop = True
        elif restart.lower() == "n":
            loop = False
        else:
            restart = input("Please input Y or N")


main()
