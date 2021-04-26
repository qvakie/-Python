def user_data(name, surname, birth, city, email, number):
    return (f'Имя: {name}, Фамилия: {surname}, Дата рождения: {birth}, Город: {city},'
            f' Email: {email}, Номер: {number}')


n, s, b, c, e, numb = input('Введите имя: '), input('Введите фамилию: '), input('Введите дату рождения: '), input('Введите город: '),\
                      input('Введите email: '), input('Введите номер: ')
print(user_data(n, s, b, c, e, numb))
