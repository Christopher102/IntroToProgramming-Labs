

class product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def purchasecount(self, count):
        self.quantity = self.quantity - count
        return self.quantity

    def totalcost(self, count):
        total = self.price * count
        return total
