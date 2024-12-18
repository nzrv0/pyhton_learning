# it's bascily working mecahnism of the bineary search "don't need to invent the wheel again"
import bisect

# this list has to be sorted
sorted_fruits = ["apple", "banana", "orange", "plum"]
# it's going to give us a position in the list of element
bisect.bisect_left(sorted_fruits, "banana")

# this going to give use the position of element where suppose to be
bisect.bisect_left(sorted_fruits, "watermelon")


# we can insort an element to the list
bisect.insort_left(sorted_fruits, "watermelon")
bisect.insort_right(sorted_fruits, "plum")
