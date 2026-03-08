class Item:
    def __init__(self, name, weight, price):
        self.__name = name
        self.__weight = weight
        self.__price = price

    def get_name(self):
        return self.__name
    
i = Item("Sword", 7, 504.34)

print(i.get_name())

