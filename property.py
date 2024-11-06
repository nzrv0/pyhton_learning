class Example:
    def __init__(self, radius):
        self._radius = radius

    def _get_value(self):
        return self._radius

    def _set_value(self, radius):
        self._radius = radius

    def _del_value(self):
        del self._radius

    radius = property(
        fget=_get_value, fset=_set_value, fdel=_del_value, doc="radius property"
    )


example = Example("10")
print(example._get_value())
# help(example)
print(dir())


class Example2:
    def __init__(self, radius):
        self._radius = radius

    # this radius value also read only we cannot change this value if we don't make setter in above
    @property
    def radius(self):
        print("get radius")  # this will be our doc value
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius


example2 = Example2("20")
print(example2.radius)
