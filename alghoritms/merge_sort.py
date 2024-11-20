def merge(left, right):
    if len(left) == 0:
        return right
    if len(right) == 0:
        return left
    resoult = []
    index_left = index_right = 0
    while len(resoult) < len(right) + len(left):
        if left[index_left] <= right[index_right]:
            resoult.append(left[index_left])
            index_left += 1
        else:
            resoult.append(right[index_right])
            index_right += 1
        if index_right == len(right):
            resoult += left[index_left:]
            break
        if index_left == len(left):
            resoult += right[index_right:]
            break

    return resoult


def merge_sort(array):
    if len(array) < 2:
        return array
    midpoint = len(array) // 2

    return merge(left=merge_sort(array[:midpoint]), right=merge_sort(array[midpoint:]))


array = [2, 4, 5, 7, 3, 8]

# left - 2, 4, 5 -> 4, 5 -> [2], [4, 5] -> [2, 4, 5]
# right - 7, 3, 8 -> 3, 8 -> [7], [3, 8] -> [3, 7, 8]
# resoult = [2, 3, 4, 5, 7, 8]

resoult = merge_sort(array)
print(resoult)
