def insert_sort(array):
    for i in range(1, len(array)):
        # right item
        keyItem = array[i]

        # left item
        j = i - 1

        # looping on the items from left to right, replacing the rigth item with the biggest value with the left item
        while j >= 0 and array[j] > keyItem:
            array[j + 1] = array[j]
            j -= 1

        # inserting the left item with the the its value from the rigth which is smaller than right item
        array[j + 1] = keyItem

    return array


array = [8, 2, 6, 4, 5]
insert_sort(array)
