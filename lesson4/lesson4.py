import random

a = 4

b = [4, 5, 6, 1, 2, 7]
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for y in c:   # сложность O(N^2) - ложный цикл
    for x in y:
        print(x, end='')
    print()

# 1, 2, 3
for i in range(a): # сложность O(N^2), ибо метод count включает в себя цикл
    print(f'{i} = {b.count(i)}')

"""СТРОКИ"""
"""получение длины строки"""
a = 'hello world'
print(len(a))  # работает одинаково для всех типов данных str, list, set, tuple,

"""получение символа строки по индексу
индексы считаются с нуля
A[от:до:шаг] параметры опциональные
от первого до третьего - A[:3]
от второго и до последнего - A[2:len(A)] = A[2:] 
каждый второй элемент A[::2]
отрицательный шаг A[::-1] = olleh"""

print(a[2:len(a)])
print(a.encode())
a = 'hello world'
"""методы поиск в строке"""
"""S.find(str,[start], [end]) - вернет индекс первого найденого элемента"""
print(a.find('world'))  # если элемент не найден - вернет "-1"
print(a.rfind('l'))  # поиск осуществляется справа налево
print(a.index('e'))   # если инлекс ничего не найдет, будет ошибка value error
print(a.rindex('e'))  # поиск справа налево

url = 'https://domain.com'
if url.startswith('https://') and url.endswith('.com'):
    print('OK')
else:
    print('error')

"""состоит ли строка из каких-то символов"""
"""
.isdigit() только из чисел
.isalpha() тольки буквы, пробел - это не буква"""

print(a.islower())  # проверка все ли цифры малого регистра

a = a.replace('o', 'O', 2)  # 2- ограниченное количесттво замен
print(a.replace('o', 'O'))

a = '1, 2, 3, 4, 5, 6'
items = a.split(', ')[:4]
# only_str_items = list(map(str, ['hello'], 'world', 2, 4, '4'))
print(items)  # по умолчанию разделитель - пробел, если не указать другой.
# разделение по делителю = ['1', '2', '3', '4', '5', '6']
new_a = '-_'.join(items)  # все элементы должны быть строками
print(new_a) # объединяет строки

a = 'Hello 2 WorlD'
print(a.upper())
print(a.lower())
print(a.title())
print(a.swapcase())
print(a.casefold())
print(a.capitalize())

"""
HELLO 2 WORLD
hello 2 world
Hello 2 World
hELLO 2 wORLd
hello 2 world
Hello 2 world
"""
print('1test'.title())

a = '  test  '  # забирает символы пробела или свои символы, только начальные или конечные символы, если спереди символ, то пробелы после символа не заберет
print(a.lstrip())
print(a.rstrip())
print(a.strip())

print('12'.zfill(4))  # добавляє нули, если строка меньшего размера чем нужно

print('{} hello'.format('23'))


"""Операции со списками  list
в списке могут быть разные типы данных, тогда как в массиве - все данные одного типа"""
items = ['Hello', 1, 2, 3, True, False]

print(items[4])

print(items[::-1])  # розвернутый список
print(len(items))

for idx in range(len(items)):
    print(items[idx])

for idx in enumerate(items):
    print(f'{idx} = {items}')

coords = [1, 10, -2, 'Operation Error', 'Index Error']
print(coords[0])
print(coords[1])
print(coords[2])

x, y, z, *_ = coords  # распаковка списка, но не сработает с другим количеством, чем длина списка
# *_ - не учитывать
# *errors - все остальные значения помещает в переменную errors


x, y, z, *errors = coords
print(x, y, z, errors)
*errors, x, y, z = coords
print(errors, x, y, z)

print(coords)
print(*coords)  # розпаковка списка в параметры

print('Index Error' not in coords)  # поиск в списке
a = [2, 1, 3, 4]
b = [3, 3]
print(a > b)
print(a >= b)
print(a == b)
print(a * 3)
print(a + b)

print(random.randint(1, 10))

items = []
for _ in range(10):
    random_number = random.randint(-10, 10)
    items.append(random_number)
print(items)

print(random.choice(coords))
print(random.choices(coords, k=4))  # выбирает все подряд и может увеличивать размер списка
print(random.sample(coords, k=4))  # выбирает уникальные элементы

map_out = list(map(float, items))
reversed_out = list(reversed(items))

print(map_out)
print(min(items))
print(max(items))
print(sorted(items, reverse=True))
print(reversed_out)
item = ['hello', None, 1, 2, False, True, None]
print(item)
filter_out = list(filter(None, item))
print(filter_out)
















