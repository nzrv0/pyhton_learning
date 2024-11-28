def fibonacci(n):
    print(n)
    if n <= 1:
        return n
    first_calc = fibonacci(n - 1)
    print(f"first calc - {first_calc} - {n}")
    second_calc = fibonacci(n - 2)
    print(f"second calc - {second_calc}")

    return fibonacci(n - 1) + fibonacci(n - 2)

# factorial(4)
    # factorial(3)
        # factorial(2)
            # factorial(1)
                # return 1
        # factorial(2) 
            # factoril(0)
    

print(fibonacci(4))
# print([fibonacci(n) for n in range(10)])
# best case O(1)
# worst case O(2^n)
# fibonnaci(5)
# fibonacci


def factorial(n):
    if n <= 1:
        return n
    first_calc = fibonacci(n - 1)
    return first_calc * n


