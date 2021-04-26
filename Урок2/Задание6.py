# Ввод данных
a = []
count = 0
while True:
    count += 1
    a.append((count, {'название': input('Введите название: '), 'цена': input("Введите цену: "), 'количество': input("Введите количество: "), 'ед': input("Введите единицы: ")}))
    print('Если хотите закончить, напишите - "stop", \nИли же напишите что угодно для продолжения')
    if input() == 'stop':
        break
# Аналитика данных
names = []
cost = []
count = []
ed = []
for i in range(len(a)):
    x = a[i]
    l = x[1]
    names.append(l['название'])
    cost.append(l['цена'])
    count.append(l['количество'])
    ed.append(l['ед'])
last_step = {'название': names, 'цена': cost, 'количество': count, 'ед': set(ed)}
print(last_step)


