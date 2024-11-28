from random import randint


def quick_sort(array):

    if len(array) < 2:
        return array

    lowest, same, highest = [], [], []
    piwot = array[randint(0, len(array) - 1)]
    for item in array:
        if item < piwot:
            lowest.append(item)
        elif item == piwot:
            same.append(item)
        elif item > piwot:
            highest.append(item)
    return quick_sort(lowest) + same + quick_sort(highest)


# best case O(nlog_2(n))
# worst case O(n**2)
