""" Задание:
1. Пользователь вводит с клавиатуры три числа в переменные a, b, c. Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no
2. Пользователь вводит с клавиатуры три числа в переменные a, b, c. Найдите наибольшее число из них и запишите в переменную max.
3. Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B."""


"""Пользователь вводит с клавиатуры три числа в переменные a, b, c. """
""" Ввод чисел """
"""Валидация ввода числа а"""
i = True
while i:
    try:
        a = int(input('Введите целое число a: '))
        i = False
    except ValueError as e:
        i = True
        print(f'Вы ввели не целое число a, ошибка: {e}')

"""Валидация ввода числа b"""
i = True
while i:
    try:
        b = int(input('Введите целое число b: '))
        i = False
    except ValueError as e:
        i = True
        print(f'Вы ввели не целое число b, ошибка: {e}')

"""Валидация ввода числа c"""
i = True
while i:
    try:
        c = int(input('Введите целое число c: '))
        i = False
    except ValueError as e:
        i = True
        print(f'Вы ввели не целое число c, ошибка: {e}')

"""Задание 1 : Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no"""
if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
    print('yes')
else:
    print('no')


""" Задание 2. Найдите наибольшее число из них и запишите в переменную max."""
if c < a > b:
    max = a
elif c < b > a:
    max = b
else:
    max = c
print(f'Найбольшее число: {max}')

""" Задание 3. 
Нужно вывести сумму всех четных чисел в диапазоне от a до b."""

summa = 0
"""Определения мінімального и максимального числа диапазона"""
if a > b:
    max_value = a
    min_value = b
else:
    max_value = b
    min_value = a

"""Суммирование четных чисел в диапазоне"""
for i in range(min_value, max_value):
    if i % 2 == 0:
        summa = summa + i

print(f'Сумма четных чисел в диапазоне от {a} до {b} равна: {summa}')