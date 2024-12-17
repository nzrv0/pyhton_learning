# Finding iterativly
def bineary_search(elements, value):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        if elements[middle] == value:
            return middle
        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > value:
            right = middle - 1


# Finding recursively


def bineary_search_rec(elements, value):
    left, right = 0, len(elements) - 1
    if left <= right:
        middle = (left + right) // 2

        if elements[middle] == value:
            return True

        if elements[middle] < value:
            return bineary_search_rec(elements[middle + 1 :], value)
        elif elements[middle] > value:
            return bineary_search_rec(elements[:middle], value)

    return False
