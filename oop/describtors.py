# this object implements descriptor protocol
class Example:
    # def __init__(self, name) -> None:
    #     # self.name = {}
    #     # --------------------------------------------
    #     self.name = name
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, type=None) -> object:
        # try:
        #     return self.name[obj]
        # except:
        #     return 0
        # --------------------------------------------
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value) -> None:
        # self.name[obj] = value
        # --------------------------------------------
        obj.__dict__[self.name] = value


class Example2:
    # when we initilize Example object it's called descriptor
    name = Example()


example = Example2()
example2 = Example2()
example3 = Example2()
example.name = "harari"
print(example.name)
print(example2.name)
print(example3.name)


# writing as a decortor
class Foo:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.func(obj)
        return obj.__dict__[self.name]


class Bar:
    @Foo
    def bar_meth(self):
        return self


foo = Bar()
print(foo.bar_meth)
