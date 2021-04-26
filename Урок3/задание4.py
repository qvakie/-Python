def my_func(x, y):
    a = 1
    for i in range(y):
        a *= x
    return x**y, a


print(my_func(int(input()), int(input())))
