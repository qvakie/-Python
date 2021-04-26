def my_func(one, two, three):
    return max(one, two, three) + ((one + two + three) - min(one, two, three) - max(one, two, three))


print(my_func(int(input()), int(input()), int(input())))