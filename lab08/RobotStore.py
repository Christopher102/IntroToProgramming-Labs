# Lab 6

# Christopher Fioti

# 11/17/2019

# This program creates a virtual store

from products import product

URF = product("Ultrasonic Range Finder", 2.50, 4)
SM = product("Servo Motor", 14.99, 10)
SC = product("Servo Controller", 44.95, 5)
MC = product("Microcontroller Board", 34.95, 7)
LRF = product("Laser Range Finder", 149.99, 2)
LPB = product("Lithium Polymer Battery", 8.99, 8)
storeproducts = [URF, SM, SC, MC, LRF, LPB]


def print_stock():
    print("\nAvailable Products")
    print("------------------")
    counter = 1
    for item in storeproducts:
        if item.quantity > 0:
            print(counter, ")", item.name, "$" + str(item.price))
            counter += 1
        else:
            print("NONE AVAILIBLE")
    print("------------------")


def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        print_stock()
        vals = input(
                "Enter product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break
        prod_id = int(vals[0]) - 1
        count = int(vals[1])
        print('''
The total cost will be ${}'''.format(storeproducts[prod_id].totalcost(count)))
        if storeproducts[prod_id].quantity < count:
            if storeproducts[prod_id].quantity == 0:
                print("Sorry, we are sold out of", storeproducts[prod_id].name)
            else:
                print("There aren't that many in the store!")
        if storeproducts[prod_id].quantity >= count:
            if cash >= storeproducts[prod_id].price:
                storeproducts[prod_id].purchasecount(count)
                cash -= storeproducts[prod_id].price * count
                print("You purchased", count, storeproducts[prod_id].name)
                print("You have $", "{0:.2f}".format(cash), "remaining.")
            else:
                print("Sorry, you cannot afford that product.")


main()
