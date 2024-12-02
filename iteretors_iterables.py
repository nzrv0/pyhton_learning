# these are the iterabels
a, b, c, d = [1, 2, 3], (1, 2, 3), {1: 1, 2: 2, 3: 3}, {1, 2, 3}


# custom iteretor
class Squences:
    def __init__(self, items) -> None:
        self.items = items
        self._next = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._next < len(self.items):
            items = self.items[self._next]
            self._next += 1
            return items
        else:
            raise StopIteration


squences = Squences([1, 2, 3, 4])

# when the first iterator was cansumed it cannot be called another time
for i in squences:
    print(i)

# we cal use iter and next protocol(dunder method)
iterator = squences.__iter__()
while True:
    try:
        item = iterator.__next__()

    except StopIteration:
        break
    else:
        print(item)

# with built in functions
nextvalue = iter(a)
print(next(nextvalue))


# this is the generator function
def iterrateover(items):
    for i in items:
        yield i
    # antoher way to write code on above
    # yield from items


# generator iterator
for i in iterrateover(b):
    print(f"this is iterrateover function values {i}")

# generator expression
gg = (i for i in range(10))
print(gg)
