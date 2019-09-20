# This function will find the value of pi then the difference from actual pi
import math


def main():
    nth = int(input("Please Enter the Nth Term You Wish To Recieve: "))
    result = (pi(nth))
    print("Sum: ", result)
    print("Difference: ", math.pi - result)


def pi(nth):
    if nth <= 0:
        print("The number has to be greater than 0")
    elif nth % 2 == 0:
        nth *= 2
    else:
        nth *= 2
        nth -= 1
    add = 0
    for i in range(1, nth, 4):
        now = (4/i)
        add += now
        after = (4/(i+2))
        add -= after
    return add


main()
