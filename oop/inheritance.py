import json


class Example:
    class_atribut = "hey there I'm class atribute"

    def __init__(self, name):
        self.name = name

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Mixin:
    def to_json(self):
        return json.dumps(self.__dict__)


class Example2(Mixin, Example):
    def __init__(self, name, surname):
        # super will call the object of it's parent and then we will initilaze the values of it's parent
        super().__init__(name)
        self.surname = surname

        atr = super().class_atribut

    # this will overwrite the get_name method
    def get_name(self):
        print(f"{self.name} {self.surname}")
        # for extending rather than overwriting method
        name = super().get_name()
        print(name)


class Example3(Example):
    def get_name(self):
        print("messsage")


class Mutliple(Example2, Example3):
    pass


exampleMixin = Example2("Father", "oh father")
exampleJson = exampleMixin.to_json()
print(exampleJson)

example = Mutliple("jesus", "christ")
example.get_name()
# example.to_json()
print(Mutliple.__mro__)
