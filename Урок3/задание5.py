def total(arg):
    global summator
    global g
    for b in arg:
        if b.isdigit():
            summator += int(b)
        else:
            g += 1
            return f'Ваша сумма = {summator}'
    return f'Ваша сумма = {summator}'


g = 0
summator = 0
while True:
    if g == 1:
        break
    a = [i for i in input().split()]
    print(total(a))




