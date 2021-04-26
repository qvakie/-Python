def my_func(digit1, digit2):
    return digit1 / digit2


try:
    print(my_func(int(input('Введите число: ')), int(input('Введите второе число: '))))
except ValueError:
    print('Пожалуйста, введите целое число')


