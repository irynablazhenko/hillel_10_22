"""
2. Написать функцию, которая возвращает список результатов выполнения заданной функции, к
соответствующим элементам переданных итерируемых объектов.
Если переданные итерируемые объекты разной длины, то результат сформировать по кратчайшему итерируемому объекту.
sum2 = lambda x, y: x + y
sum3 = lambda x, y, z: x + y + z
assert custom_map(sum, [[1, 2, 3], [4, 5]]) == [6, 9]
assert custom_map(len, [[], (2, 4), [1, 3, 5, 7]]) == [0, 2, 4]
assert custom_map(str, (17, 23)) == ['17', '23']
assert custom_map(sum2, [1, 2, 3], [3, 5, 0]) == [4, 7, 3]
assert custom_map(sum2, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)) == [4, 6, 7, 8]
assert custom_map(sum3, [1, 1, 1], [4, 5, 6], [0, 5, 2, 1]) == [5, 11, 9]

Встроенную функцию map не используем.

def custom_map(function: Callable, *iterables: Iterable) -> Iterable:
  pass
"""
# -------------------------------------------------------------------------------------------------------------
import functools

sum2 = lambda x, y: x + y
sum3 = lambda x, y, z: x + y + z


def custom_map(function, *iterables):
    result = []
    min_len = 0
    for i in iterables:
        if min_len == 0 or len(i) < min_len:
            min_len = len(i)

    for i in range(min_len):
        args = []
        for j in iterables:
            args.append(j[i])
        result.append(function(*args))

    return result


print(f'Результат функции Len : {custom_map(len, [[], (2, 4), [1, 3, 5, 7]])}')
print(f'Результат функции sum2 : {custom_map(sum2, [1, 2, 3], [3, 5, 0])}')
print(f'Результат функции sum2 : {custom_map(sum2, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44))}')
print(f'Результат функции sum3 : {custom_map(sum3, [1, 1, 1], [4, 5, 6], [0, 5, 2, 1])}')
print(f'Результат функции sum : {custom_map(sum, [[2, 4], [1, 3, 5, 7]])}')
print(f'Результат функции str : {custom_map(str, (17, 23))}')
print(f'Результат функции sum : {custom_map(sum, [[2, 4], [1, 3, 5, 7]])}')

assert custom_map(sum, [[1, 2, 3], [4, 5]]) == [6, 9]
assert custom_map(len, [[], (2, 4), [1, 3, 5, 7]]) == [0, 2, 4]
assert custom_map(str, (17, 23)) == ['17', '23']
assert custom_map(sum2, [1, 2, 3], [3, 5, 0]) == [4, 7, 3]
assert custom_map(sum2, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)) == [4, 6, 7, 8]
assert custom_map(sum3, [1, 1, 1], [4, 5, 6], [0, 5, 2, 1]) == [5, 11, 9]

