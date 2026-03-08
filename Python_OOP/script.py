class Item:
    def __init__(self, name, weight, price):
        self.__name = name
        self.__weight = weight
        self.__price = price

    def get_name(self):
        return self.__name
    
    def __str__(self):
        return f"{self.__name} ({self.__weight}kg) - {self.__price} gold"

i = Item("Sword", 7, 53)

print(i)

