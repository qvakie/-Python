# Задание Номер 4
a = input().split(' ')
for i in range(len(a)):
    b = a[i]
    if len(b) > 10:
        print(i, b[:10])
    else:
        print(i, b)