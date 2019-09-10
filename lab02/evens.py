# This Program prints out all the evens in a series of numbers
# I borrowed some code I found online to make this easier


def main():
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    for n in list1:
        if n % 2 == 0:
            print(n)

main()
