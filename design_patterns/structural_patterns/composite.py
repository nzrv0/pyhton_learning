from abc import ABC, abstractmethod


class Item(ABC):
    @abstractmethod
    def return_price(self):
        pass


class Phone(Item):
    def __init__(self, price):
        self.price = price

    def return_price(self):
        return self.price


class Charger(Item):
    def __init__(self, price):
        self.price = price

    def return_price(self):
        return self.price


class Earphones(Item):
    def __init__(self, price):
        self.price = price

    def return_price(self):
        return self.price


class Box(Item):
    def __init__(self, contents):
        self.contents = contents

    def return_price(self):
        price = 0
        for item in self.contents:
            price += item.return_price()
        return price


# one box
phone_case_contents = []
phone_case_contents.append(Phone(200))
phone_case_box = Box(phone_case_contents)

# many boxes
big_box_contents = []
big_box_contents.append(phone_case_box)
big_box_contents.append(Charger(10))
big_box_contents.append(Earphones(10))
big_box = Box(big_box_contents)

print("Total price: " + str(big_box.return_price()))
