# CMPT 120 Intro to Programming
# Lab 5 - Working with Strings and Functions
# Author: Chris Fioti
# Created: 2019-10-03

import re


def names():
    first = input("Please enter your first name: ").lower()
    last = input("Please enter your last name: ").lower()
    fullname = [first, last]
    return fullname


def user(fullname):
    userN = str(fullname[0] + "." + fullname[1] + "1")
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


def passwordcaptial(passwd):
    if passwd.lower() == passwd:
        print("Please use capitals in your password!")
        return passwordcaptial(passwordlength(password()))
    elif passwd.upper() == passwd:
        print("Please use lowercase in your password!")
        return passwordcaptial(passwordlength(password()))
    else:
        print("The force is strong with this one.")
        return passwd


def main():
    Username = user(names())
    passfinal = passwordcheck(password())
    print("Account Created. Your new email is " + Username + "@marist.edu")


main()
