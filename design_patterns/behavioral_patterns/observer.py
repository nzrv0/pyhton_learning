from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class Subject(ABC):
    """
    The Subject interface declares a set of methods for managing subscribers.
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


# Concrete subject class
class StockMarket(Subject):
    observers = []

    def __init__(self, name):
        self.name = name
        self.price = None

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def set_price(self, price):
        self.price = price
        self.notify()


# Concrete observer class
class StockTrader(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, subject):
        print(f"{self.name} received new price: {subject.price}")


market = StockMarket("NASDAQ")
trader1 = StockTrader("John")
trader2 = StockTrader("Jane")

market.attach(trader1)
market.attach(trader2)

market.set_price(100.0)

market.detach(trader2)

market.set_price(200.0)
