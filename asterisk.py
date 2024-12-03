# positional only arguments
def func(var1, var2, /):
    print(var1, var2)


# this code will give a error func(2, var2=3)
func(2, 3)


# keyword only arguments
def func2(*, var1, var2):
    print(var1, var2)


# this code will give a error func(2, var2=3)
func2(var1=2, var2=3)


# additonal this works as the keyword only
def func3(*args, var1, var2):
    print(args, var1, var2)


func3(1, 2, 3, var1=3, var2=3)
