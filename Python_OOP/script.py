class Item:
    def __init__(self, name, weight, price):
        self._name = name
        self._weight = weight
        self._price = price

    def get_name(self):
        return self._name
    
    def __str__(self):
        return f"{self._name} ({self._weight}kg) - {self._price} gold"

class Weapon(Item):
    def __init__(self, name, weight, price, damage):
        super().__init__(name, weight, price)
        self._damage = damage

    def __str__(self):
        return f"{self._name} ({self._weight}kg) - {self._price} gold, {self._damage} damage"

i = Weapon("Sword", 7, 53, 11)

print(i)

