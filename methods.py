class Example:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        cordinates = (self.x, self.y, self.z)
        yield from cordinates

    # this is insteance method
    def getNameOfObject(self):
        return type(self)

    @staticmethod
    def show_coridantes(name):
        print(f"hey {name}, how are you")

    @classmethod
    def from_iter(cls, iter):
        return cls(*iter)

    # def __str__(self) -> str:
    #     return "{}-{}-{}".format(self.x, self.y, self.z)

    def getName(self):
        return self.x


example = Example("10", "20", "40")
example.show_coridantes("Harrari")
for index, item in example:
    print(f"{index}-{item}")
cordinates = (3, 4, 5)
iterrated = example.from_iter(cordinates)
print(iterrated)

print(isinstance(example, Example))

example2 = example.getNameOfObject()
example2.__init__(example, "20", "20", "20")

print(example2.getName(example))
print(example)
