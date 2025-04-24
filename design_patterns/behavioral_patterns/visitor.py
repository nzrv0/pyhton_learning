from abc import ABC, abstractmethod


class Element(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass


class Book(Element):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def accept(self, visitor):
        visitor.visit_book(self)


class Fruit(Element):
    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight

    def accept(self, visitor):
        visitor.visit_fruit(self)


class Visitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_fruit(self, fruit):
        pass


class TaxVisitor(Visitor):
    def visit_book(self, book):
        book.price *= 1.10

    def visit_fruit(self, fruit):
        fruit.price *= 1.05


class DiscountVisitor(Visitor):
    def visit_book(self, book):
        book.price *= 0.90

    def visit_fruit(self, fruit):
        fruit.price *= 0.95


book = Book("The Hitchhiker's Guide to the Galaxy", 25.0)
fruit = Fruit("Apple", 1.0, 0.5)

tax_visitor = TaxVisitor()
discount_visitor = DiscountVisitor()

book.accept(tax_visitor)
fruit.accept(tax_visitor)

book.accept(discount_visitor)
fruit.accept(discount_visitor)

print(f"{book.name} price after tax and discount: {book.price}")
print(f"{fruit.name} price after tax and discount: {fruit.price}")
