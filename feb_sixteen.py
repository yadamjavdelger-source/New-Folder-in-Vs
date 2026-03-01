class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


item1 = Item("Ezio", 999)

class ShoppingCart:
    def __init__(self):
        self.items = [] 
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def showItem(self):
        for item in self.items:
            print(item.name, item.price)

cart1 = ShoppingCart()
cart1.addItem(item1)
cart1.showItem()




