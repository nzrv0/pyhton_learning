var = ""


def main():
    global var
    var += "face"
    temp = 0

    # enclosing or nonclosing scope
    def inner():
        # cannot define nonlocal in global or in the local(funciton) scope, only in the enclosing scope
        nonlocal temp
        return temp

    return inner


var = main()
print(var())


# there're other scope which callign buitlitn scope we can acccses it from anywere without or within improting it
# print(dir(__builtins__))


# closure
def outof(var):
    def inner(var2):
        return var2**2 + var

    return inner


# closures not forgetting the previus value which you passed in
var1 = outof(12)
print(var1(39))
print(var1(32))
