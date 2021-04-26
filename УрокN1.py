# Задание N. 1
lovely_color = input('Введите ваш любимый цвет: ')
if lovely_color.lower() == 'сиреневый':
    print('Взаимно')
age = int(input('Сколько вам лет?: '))

# Задание N. 2
time = int(input())
hours = time // 3600
minutes = hours // 60
seconds = minutes // 60
if minutes < 10:
    minutes = '0' + str(minutes)
if hours < 10:
    hours = '0' + str(hours)
if seconds < 10:
    seconds = '0' + str(seconds)
print(f'{hours}:{minutes}:{seconds}')

# Задание N. 3
n = int(input('Введите число: '))
total = 0
for i in range(1, n + 1):
    total += int(i * '3')
print(total)

#Задание N. 4
n = int(input('Введите целое положительно число: '))
maxi = 0
for i in str(n):
    maxi = max(int(i), maxi)
print(maxi)
# через while
n = int(input())
maxa = 0
while n > 0:
    if n % 10 > maxa:
        maxa = n % 10
    n //= 10
print(maxa)
# Через что то более прикольное
n = ' '.join(input()).split()
print(max(n))

#Задание N. 5
v, iz = int(input("Введите выручку: ")), int(input("Введите издержки: "))
rent = 0
if v > iz:
    rent = ((v - iz) / v) * 100         #не уверен по поводу формулы
    print(f'Прибыль, Ваша рентабельность - {rent}%')
    b = int(input("Введите количество работников: "))
    print(f'Доля прибыли на каждого работинка = {(v - iz) // b}')
else:
    print('Убыток :(')

#Задание N.6
a, b = [int(input('Введите данные: ')) for _ in range(2)]
day = 1
print(f'{day}-ый день: {a}')
while True:
    day += 1
    a += a * 0.1
    print(f'{day}-ый день: {round(a, 2)}')
    if a >= b:
        break
print('Мои поздравления!')
