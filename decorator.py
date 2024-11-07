# Put simply, a decorator wraps a function, modifying its behavior.
import functools


def giveone(
    func,
):
    @functools.wraps(func)
    def wrapper_giveone(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper_giveone


@giveone
def takeone(value):
    print(f"this is the one of the value {value}")
    return f"{value}"


@giveone
def taketwo(value):
    print(f"this is the two of the value {value}")


print(
    takeone.__name__
)  # without functools.wraps decorator will be this value: wrapper_giveone
one = takeone(1)
print(one)

taketwo(2)


# this is simply a decorator
# one = giveone(takeone)

# print(one)


# def example(func, args):
#     return func(args)


# def example2(var):
#     return f"{var}"


# var = example(example2, "hey")
# example2("3")
# print(var)


# optional decorator
def repeat(_func=None, num_times=2):
    print(f"this is inner function {_func}")

    def decoretor_func(func):
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    if _func == None:
        return decoretor_func
    else:
        return decoretor_func(_func)


@repeat(num_times=3)
def say_hello(value):
    print(f"Hi {value}")


@repeat
def say_by(value):
    print(f"By {value}")


# say_hello("Bob")
# say_by("Bob")


# using classes as a decoretor
class Example:
    def __init__(self, func) -> None:
        self.func = func
        self.count = 0

    def __call__(self):
        self.count += 1
        print(f"{self.count}-{self.func.__name__}()")
        return self.func


@Example
def say_hi():
    print("hi")


say_hi()
say_hi()
say_hi()
