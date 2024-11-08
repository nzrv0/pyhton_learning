# this is simple bubble sort alghoritm

# list_items = [3, 4, 5, 6, 1]


def buble_sort(array):
    n = len(array)
    already_sorted = True
    for i in range(n):
        # length of 5 stopping at 4
        for index in range(n - i - 1):
            if array[index] >= array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                already_sorted = False
        if already_sorted:
            break
    return array


# in the best case O(n)
# in the worst and avarge case O(n^2)
