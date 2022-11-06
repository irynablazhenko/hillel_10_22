import random


# #  print([random.randomint(1,10) for _ in range(10)])
numbers = [5, 10, 3, 6, 8, 2, 5, 66, 73]
print(numbers)
a = numbers.pop()  # удаляет все элементы кроме последнего
print(numbers)
print(a)

# del numbers[1]  # удаляет єлемент из списка, главное, чтобы не выйти за рамки
# # можно удалять и переменные и целые списки
# del numbers  # удаляет список
#
#
# print([random.randomint(1, 10) for _ in range(10)])
# print(numbers)
#
# values = []
# for _ in range(4):
#     numbers = int(input('Enter a number: '))
#     values.append(numbers)
#    # values.insert(0, numbers)  Добавляет с указанного індекса указанное значение
#
# print(values)
#
# print(values.count(4))
# print(values.insert(1))  # поиск по значению, возвращает ындекс позиции
#
# print(1 in values)
# print(values)
# # print(1 is values)  # сравнивает это тот же объект или нет. Проверяет по ссылке
#
# a = 1
#
# print(1 is a)
# a = [1]
# b = [1]
# # print(a is b)
# print(hex(id(a)), hex(id(b)))
#
# # перезаписать элемент списка
# numbers[1] = 2

import copy


a = [1, 2, ['Hello', 'world'], 3, 4]
b = copy.deepcopy(a)
print(a is b)

print(a, b)
b.append(5)
b[2].append(False)
print(a, b)

# list comprehension
#  x for x in range(10) if x < 5

# numbers = [[random.randomint(1, 10),i] for i in range(10) if i % 2 == 0]

numbers = [x for x in numbers if x < 5]
print(numbers)

# tuple тот же список, только он не изменяеться. У него нету методов append, insert...
a = (1, )  # кортеж з одного елементу або a = 1,
print(type(a), a)

a = (1, 2, 3, 4)
print(a[::-1])
print(a)
# a[2] = 4  # будет ошибка
# всего 2 метода count и index
print(a.count(2))
print(a.index(3))
print(len(a))
a = a + (1, 2)  # по новій ссилці буде створено новий кортеж а

# может содержать в себе изменяемые объекты
a = (1, 2, [3, 4], False)
a[2].append(5)
print(a)
try:
    a[2] += [5, 6]
except TypeError as e:
    print(e)
print(a)

a[2].extend([7, 8])
print(a)
a = [1, 2, 3]
b = [3, 4]

# set множество - контейнер -э не может быть одинаковых елементов,
# не можем в него записать список.
# МОжно вложить только неизменяемые элементы
# используют когда наличие элемента важнее чем его порядок

a = {11, 22, 34, 22}

a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))  # возващает тру если нету одинаковых елементов
print(a == b)

a = {3, 2, 6}
b = {2, 3, 6, 5, 8}
print(a <= b)  # все элементы а входят в b
print(b.issuperset(b))
print(a.issubset(b))

# объединить множества
print(a | b)  # или a.union(b)

print(a.intersection(b))
print(a.difference(b))  # возвращает элементы, которые есть в а но нету в b, или другой синтаксис а - b


numbers = [random.randint(1, 10) for _ in range(10)]
print(numbers)
print(set(numbers))
print(len(numbers) -len(set(numbers)))

