from random import randint
from timeit import repeat
from buble_sort import buble_sort
from recursive import fibonacci
import sys


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=1)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    ARRAY_LENGTH = 1000
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    run_sorting_algorithm(algorithm=sys.argv[1], array=array)
