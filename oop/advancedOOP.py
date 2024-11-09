# Composition which represents a has-a relationship between classes.
class Robot:
    # this kind of implimentation from outside of calling object is dependiciy injection
    # def __init__(self, body) -> None:
    #     self.body = body

    def __init__(self) -> None:
        self.body = Body()

    def rotate_body_left(self, degress=20):
        self.body.rotate_right(degress)


class Body:
    def __init__(self) -> None:
        self.rotation = 0

    def rotate_left(self, degress):
        self.rotation -= degress
        print(self.rotation)

    def rotate_right(self, degress):
        self.rotation += degress
        print(self.rotation)


# Delegation you can represent can-do relationships
import json
import pickle


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Serializer:
    def __init__(self, instance):
        self.instance = instance

    def to_json(self):
        return json.dumps(self.instance.__dict__)

    def to_pickle(self):
        return pickle.dumps(self.instance.__dict__)


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __getattr__(self, attr):
        return getattr(Serializer(self), attr)


employee = Employee("john", 12, 320)
aa = employee.to_json()
print(aa)


# Abstract Base Classes(ABC)
# In a sense, ABCs work as templates for other classes to inherit from.
# you have to implement all of the methdos in your child classes from paretn
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        pi = 3.14
        return pi * self.radius**2
