"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы)
и выполняющую их деление. Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль (try except).

Пример:
Введите первое число: 10
Введите второе число: 0
Вы что? Пытаетесь делить на 0!

Process finished with exit code 0

Пример:
Введите первое число: 10
Введите второе число: 10
1.0

Process finished with exit code 0
"""
def my_func():
    try:
        x = int(input('Введите x'))
        y = int(input('Введите y'))
        z = x / y
    except ZeroDivisionError:
        print('Вы ввели y=0')
        return 'Деление на ноль запрещено'
    return z
print(my_func())

