"""Factories are used to encapsulate the information about classes we're using while instantiating them based on certain parameters we provide them with.

By using a factory, we can switch out an implementation with another by simply changing the parameter that was used to decide the original implementation in the first place.

This decouples the implementation from the usage in such a way that we can easily scale the application by adding new implementations and simply instantiating them through the factory - with the exact same codebase.

If we just get another factory as a parameter, we don't even need to know which class it produces. We just need to have a uniform factory method that returns a class guaranteed to have a certain set of behaviors. """

from abc import ABC, abstractmethod


class Product(ABC):

    @abstractmethod
    def calculate_risk(self):
        pass


class Worker(Product):
    def __init__(self, name, age, hours):
        self.name = name
        self.age = age
        self.hours = hours

    def calculate_risk(self):
        return self.age + 100 / self.hours

    def __str__(self):
        return self.name + " [" + str(self.age) + "] - " + str(self.hours) + "h/week"


class Unemployed(Product):
    def __init__(self, name, age, able):
        self.name = name
        self.age = age
        self.able = able

    def calculate_risk(self):
        if self.able:
            return self.age + 10
        else:
            return self.age + 30

    def __str__(self):
        if self.able:
            return self.name + " [" + str(self.age) + "] - able to work"
        else:
            return self.name + " [" + str(self.age) + "] - unable to work"


class PersonFactory:
    def get_person(self, type_of_person):
        if type_of_person == "worker":
            return Worker("Oliver", 22, 30)
        if type_of_person == "unemployed":
            return Unemployed("Sophie", 33, False)


factory = PersonFactory()

product = factory.get_person("worker")
print(product)

product2 = factory.get_person("unemployed")
print(product2)
