# Изначально не так прочитал задание и немного усложнил
month = int(input('Введите номер месяца: '))
# через список
spisok = ['1:Январь - Зима', '2:Февраль - Зима', '3:Март - Весна', '4:Апрель - Весна', '5:Май - Весня', '6:Июнь - Лето',
          '7:Июль - Лето', '8:Август - Лето', '9:Сентябрь - Осень', '10:Октябрь - Осень', '11:Ноябрь - Осень',
          '12:Декабрь - Зима']
print(spisok[month - 1])
# Через словарь
print('И через словарь')
my_dict = dict(item.split(':') for item in spisok)
vremya_goda = dict()
print(my_dict[str(month)])