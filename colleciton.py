import collections


### named tuple
Collect = collections.namedtuple(
    "Collect", "first second", defaults=["", "Python developer"]
)
col = Collect("Hey there")
col.first
getAsDict = col._asdict()
divmod(10, 2)  # 5 - and this is integer, 0 - this is mod


### queue
queue = collections.deque(
    ["firs", 2, "face"], maxlen=2
)  ## it's only gonna give to us as much as items was given in the maxlen
queueOther = collections.deque("abscd")  # deque(['a', 'b', 'c', 'd'])
# extend can add more iterables to the given queue
defaultQueue = collections.deque()
defaultQueue.append("anything")
defaultQueue.appendleft("pop this")
defaultQueue.popleft()
queue.rotate()

### default dictionary
defaultDict = collections.defaultdict(list)
names = [("Men", "james"), ("Woman", "Bille"), ("Men", "Hofman")]
for sex, name in names:
    defaultDict[sex].append(name)


### Ordered dictionary
orderedDict = collections.OrderedDict()
orderedDict["People"] = "first human"

## must be in order
letters_0 = collections.OrderedDict(a=1, b=2, c=3, d=4)
letters_1 = collections.OrderedDict(b=2, a=1, d=4, c=3)
letters_2 = dict(a=1, b=2, c=3, d=4)
print(letters_0 == letters_2, letters_2 == letters_1)


### count over dict elements
counter = collections.Counter("asbcdf")
counterDict = collections.Counter({"daf": 2, "dd": 2})  # values shoul be in integer
counter["a"] = 4  # this is gonna replace
counter.update(a=4)  # this is gonna sum 4 with init value

print(counter)
