# CMPT-120 Lab #6
# CHRISTOPHER FIOTI
# 10/17/2019

import re
import sys


def show_intro():
    print("Welcome to Arithmetic Engine!")
    print("="*25, '\n')
    print("Valid comments are 'add', 'sub', 'mult', 'div', and 'quit'.\n")


def show_outro():
    print("\nThank you for using the Arithmetic Engine...")
    print("\nPlease come again soon!")


def testnum(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("\nPlease enter numbers only.\n")


def do_loop():
    while True:
        cmd = input("What computation do you want to preform?: ").lower()
        if cmd == "quit":
            break
        else:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
                if cmd == "add":
                    print(num1 + num2)
                elif cmd == "sub":
                    print(num1 - num2)
                elif cmd == "mult":
                    print(num1 * num2)
                elif cmd == "div":
                    print(num1 / num2)
                else:
                    print("\nThat is not a valid command.")
            except ValueError:
                print("Please enter a number")


def main():
    show_intro()
    do_loop()
    show_outro()


main()
