import numpy as np
from numpy import newaxis

# An ndarray is a (usually fixed-size) multidimensional container of items of the same type and size.
three_dim = np.array(
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]]
)

# shape is indicating as [n,m] which is n rows and m columns
print(
    three_dim.ndim,
    three_dim.shape,
    three_dim.size,
    three_dim.dtype,
    three_dim.itemsize,
    three_dim.data,
)

# creating np array types
np.array([(1, 2, 3), (4, 5, 6)], dtype=complex)
np.zeros((3, 4))
np.ones((3, 3, 4), dtype=np.int16)
cc = np.empty((3, 4))  # creates random values
np.arange(start=10, stop=30, step=5)  # similar with range
np.linspace(start=0, stop=2, num=9)
np.arange(6).reshape(2, 3)
np.exp(cc * 1j)


# operations

a = np.array([20, 19, 30, 10])
b = np.array([20])
# print(a - b, a**2, 10 * np.sin(a), a < 20)

A = np.array([[1, 1], [0, 1]])
B = np.array([[2, 0], [3, 4]])
# print(A * B, A @ B, A.dot(B), sep="\n\n")

rg = np.random.default_rng(12)

d = np.ones((2, 3), dtype=int)
e = rg.random((2, 3))

d *= 3
e += d
# print(d, e, sep="\n\n")
# print(d.sum(), a.min(), a.max())


examp = np.arange(12).reshape(3, 4)
# print(examp.sum(axis=1), examp, sep="\n")

np.random.seed(0)  # makes random numbers predictable, new usage default_rng()
dd = np.random.randint(1, 100, size=(5, 3))
# print(dd)


# NumPy provides familiar mathematical functions such as sin, cos, and exp. In NumPy, these are called “universal functions” (ufunc).
np.sin(a)
np.cos(b)
np.exp(a)
cc = np.add(a, b)
# print(cc)


# Shape manipulation
lb = np.floor(10 * rg.random((3, 4)))

# following three commands all return a modified array, but do not change the original array:
lb.ravel()  # from 2 dimensions to 1, flattened array
lb.resize((2, 6))  # changes the original array
lb.reshape(6, 2)  # creates new array of changed values
lb.T  # transpore of n dimensional array


ex1 = np.floor(10 * rg.random((2, 2)))
ex2 = np.floor(10 * rg.random((2, 2)))
np.vstack((ex1, ex2))  # appending in vertical axios
np.hstack((ex1, ex2))  # appending in horizontal axios


np.column_stack((ex1, ex2))  # for 2d arrays
a1 = np.array([4.0, 2.0])
b2 = np.array([3.0, 8.0])
np.column_stack((a1, b2))

a1[:, newaxis]  # returs 1 dimensional as a2 dim

np.hsplit(
    lb, 3
)  # split an array along its horizontal axis, either by specifying the number of equally shaped arrays to return, or by specifying the columns after which the division should occur

np.hsplit(lb, (3, 4))  # Split `a` after the third and the fourth column


# Copies and views
cc = a1  # here is not a copy made
cc is a1  # True


def func(x):  # ids will be same
    id(x)


id(a1)
func(a1)


c = a1.view()  #  # c is a view of the data owned by a1
c is a1  # False
c.base is a1  # False
c.flags.owndata  # false
c = c.reshape((2, 6))  # a1's shape doesn't change, reassigned c is still a view of a
c[0, 4] = 1234  # a1's data changes


d1 = a1.copy()  # The copy method makes a complete copy of the array and its data.
d is a  # false
d.base is a  # false


# Indexing
examp2 = np.arange(12) ** 2

examp2[2:5]  # we can interate over, slice, change values for index number


def f(x, y):
    return 10 * x + y


ll = np.fromfunction(f, (5, 4), dtype=int)
# print(ll[...], ll[:])


for el in a.flat:  # for iterating over the values
    # print(el)
    pass


i = np.array([1, 1, 3, 8, 5])
j = np.array([[3, 4], [9, 7]])
# print(examp2[i], examp2[j], sep="\n")


# When the indexed array a is multidimensional, a single array of indices refers to the first dimension of a
palette = np.array([[0, 0, 0], [255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 255, 255]])
image = np.array([[0, 1, 2, 0], [0, 3, 4, 0]])
palette[image]
image[(0, 3)]


ed1 = np.arange(5)
ed1[[1, 3, 4]] = 0
ed1[[0, 0, 2]] = [1, 2, 3]
a[[0, 0, 2]] += 1  # 0 is done once not a twice

a12 = np.arange(12).reshape(3, 4)
a12[a12 > 4]


bd1 = np.array([False, True, True])  # first dim selection
bd2 = np.array([True, False, True, False])  # second dim selection
a12[bd1, :]  # selecting rows
a12[:, b2]  # selecting columns
a12[bd1, bd2]


# Tricks and tips
