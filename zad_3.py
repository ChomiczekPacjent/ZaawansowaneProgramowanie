class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address


class House(Property):
    def __init__(self, area, rooms: int, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (f'Dom: {self.address}, powierzchnia {self.area} m², '
                f'pokoje: {self.rooms}, działka {self.plot} m², '
                f'cena {self.price} zł')


class Flat(Property):
    def __init__(self, area, rooms: int, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (f'Mieszkanie: {self.address}, powierzchnia {self.area} m², '
                f'pokoje: {self.rooms}, piętro {self.floor}, '
                f'cena {self.price} zł')


house = House(150, 5, 850000, 'Bytom, ul. Leśna 12', 600)
flat = Flat(52, 3, 420000, 'Katowice, ul. Mariacka 5/14', 3)

print(house)
print(flat)
