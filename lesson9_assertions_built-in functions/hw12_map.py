"""
2. Написать функцию, которая возвращает список результатов выполнения заданной функции, к
соответствующим элементам переданных итерируемых объектов.
Если переданные итерируемые объекты разной длины, то результат сформировать по кратчайшему итерируемому объекту.
custom_map(sum, [1, 2, 3], [3, 5, 0, 5]) -> [4, 7, 3]

Встроенную функцию map не используем.

def custom_map(function: Callable, *iterables: Iterable) -> Iterable:
  pass
"""
# -------------------------------------------------------------------------------------------------------------
import functools

a = [2, 5, 4, 45]
b = [45, 5, 7, 465, 7]
c = [1, 5, 9, 13]
d = [3, 45, 7, 4, 6, 8, 44]

summary = lambda x, y: x + y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y
difference = lambda x, y: x - y
# exponentiation = lambda x, y: x ** y
min = lambda x, y: x if x < y else y
max = lambda x, y: x if x > y else y


def custom_map(function, *iterables):
    list_of_iterables = list(zip(*iterables))
    i = 0
    result = []
    while i < len(list_of_iterables):
        i_element = list(list_of_iterables[i])
        result.append(functools.reduce(function, i_element))
        i += 1
    # print(result)

    return result

print(f'Результат функции суммирования: {custom_map(summary, a, b,c,d)}')
print(f'Результат функции вычитание: {custom_map(difference, a, b,c,d)}')
print(f'Результат функции умножения: {custom_map(multiplication, a, b,c,d)}')
print(f'Результат функции деления: {custom_map(division, a, b,c,d)}')
# print(f'Результат функции возведения в степень: {custom_map(exponentiation, a, b,c,d)}')
print(f'Результат функции поиск минимального значения: {custom_map(min, a, b,c,d)}')
print(f'Результат функции поиск максимального значения: {custom_map(max, a, b,c,d)}')



