# THis program calculates interest costs and APR




def main():
    Years = 0
    Interest = float(input("Please enter your interest rate: "))
    Principal = float(input("Please input the starting cost: "))
    while Principal > 0:
        Principal = int(Principal - (Principal * Interest))
        Years += 1

    print(Principal)
    print(Years)


main()