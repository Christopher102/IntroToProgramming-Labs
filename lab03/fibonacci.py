# This program will be able to tell you the value of any number
# in a fibonacci sequence


def main():
    num = int(input("Enter nth number for fibonacci sequence: "))
    result = fibonacci(num)
    print(result)


def fibonacci(n):
    if n < 0:
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


main()
