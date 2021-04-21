# Задание Номер 2
a = ['Privet', None, True, 1232]
for i in range(0, len(a), 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(a)