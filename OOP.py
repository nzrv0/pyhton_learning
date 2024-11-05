# classes are great when you must bundle data and behavior together in a single entity.
class Human:
    name = "Harrari"  # class atribute

    # when object was create this dunder method will call and initlizae the values in it
    def __init__(self, nouse, eye):  # instance atribute
        self.nouse = nouse
        self.eye = eye
        self._nouse = 3  # this is private atribute
        self.__mangle = "this is mange type of naming"
        Human.name = "will change value of name"
        # another example to above, value of type will be Human class
        type(self).name = "this also will change value of name"

    def change_eye(self, eye):
        # we can also initiliza the value of the self in any method but it's praticale to use it inside init
        self.brows = "thick"
        self.eye = eye

    def get_eye(self):
        return self.eye

    # self will accses to name value because self is the object
    def get_name(self):
        return f"{self.name}"

    # still can be accsesed from the outside but name of the class defins it as non public
    def _private():
        return "this is private methdod"

    # if not defind will class insteance string depend on repr funciton
    def __str__(self) -> str:
        return self.eye

    def __repr__(self) -> str:
        class_name = type(self).__name__
        return f"{class_name}"

    # name mangling
    def __method(self):
        print(self.eye)


human = Human("your nouse", "Red")
human.change_eye("Blue")

print(human.name)
"""this also will change value of name"""

# built in funciton rather than class like a string <class str>
print(repr(human))
print(human.get_name())

# <class str>
print(type("str()"))

# it's purpose is that you can add additional functionalty to object rather than calling it in this way
print(human.__repr__())

# representing reper and string in format
print(f"{human!s}")
print(f"{human!r}")


# this gonna give as  atribute error
# print(human.__method)


# this gonna give us all of the atributes in class within dictionary
print(vars(human))
"""
{'nouse': 'your nouse', 'eye': 'Blue', '_nouse': 3, '_Human__mangle': 'this is mange type of naming', 'brows': 'thick'}
"""

# mapping all of the memmbers associted with object
print(vars(Human))
""" {'__module__': '__main__', 'name': 'this also will change value of name', '__init__': <function Human.__init__ at 0x7c16f2d20c20>, 'change_eye': <function Human.change_eye at 0x7c16f2d21d00>, 'get_eye': <function Human.get_eye at 0x7c16f2d22020>, 'get_name': <function Human.get_name at 0x7c16f2d220c0>, '_private': <function Human._private at 0x7c16f2d22160>, '__str__': <function Human.__str__ at 0x7c16f2d22200>, '__repr__': <function Human.__repr__ at 0x7c16f2d222a0>, '_Human__method': <function Human.__method at 0x7c16f2d22340>, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None}"""

# this will give us methods and atributes of class
print(Human.__dict__)
""" {'__module__': '__main__', 'name': 'this also will change value of name', '__init__': <function Human.__init__ at 0x7c16f2d20c20>, 'change_eye': <function Human.change_eye at 0x7c16f2d21d00>, 'get_eye': <function Human.get_eye at 0x7c16f2d22020>, 'get_name': <function Human.get_name at 0x7c16f2d220c0>, '_private': <function Human._private at 0x7c16f2d22160>, '__str__': <function Human.__str__ at 0x7c16f2d22200>, '__repr__': <function Human.__repr__ at 0x7c16f2d222a0>, '_Human__method': <function Human.__method at 0x7c16f2d22340>, '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None}"""

# adding atributes and methods to class dynamicly
human.ear = "too long"


def __init__(self, face):
    self.face = face


human.__init__ = __init__
setattr(human, "hands", "two hands")

print(human.__dict__)
"""
{'nouse': 'your nouse', 'eye': 'Blue', '_nouse': 3, '_Human__mangle': 'this is mange type of naming', 'brows': 'thick', 'ear': 'too long', '__init__': <function __init__ at 0x75d843921d00>, 'hands': 'two hands'}
"""
