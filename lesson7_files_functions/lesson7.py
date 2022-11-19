# numbers = [9, 1, 2, 5, 7, 3]
# count = 0
# for i in range(len(numbers)):
#     if numbers[i] == numbers[i + 1]:
#         count += 1
#
# print(count)

def get_max_number(a, b, c):
    print((f'A = {a} | B = {b} | C = {c}'))
    if a > b and a > c:
        return f'A = {a}'
    elif b > a and b > c:
        return f'B = {B}'
    elif c > a and c > b:
        return f'C = {c}'
    else:
        return 'A = B = C'

max_number = get_max_number(5, 4, 8)
print(max_number)
print(get_max_number(2353, 523, 523))
print(get_max_number(253, 53, 352))
print(get_max_number(3, 43, 538))

def greetings(name):
    print(f'Hello {name}')

def output_1(result):
    print('-----')
    print(f'|{str(result).zfill(4)}|')
    print('-----')

def math_func(a, b, out_func):
    c = a ** b
    out_func()

# math_func(5, 6, output_1)

def default_args(a, b=None, c=None):
    print(f'A = {a} | B = {b} | C = {c}')

default_args(1, 2, 3)
default_args(1)
default_args(1, 2)
#  можно прописывать
default_args(c=1, a=2)

def list_sum(numbers=[]):  # неправильно так объявлять значение по дефолту для мутебел типам
    numbers.append(1)
    print(sum(numbers))

list_sum([1, 2, 3])
list_sum()  # 1
list_sum()  # 2
list_sum()  # 3

"""правильно"""
def list_sum1(numbers=None):  # неправильно так объявлять значение по дефолту для мутебел типам
    if numbers is None:
        numbers = []
    numbers.append(1)
    print(sum(numbers))

list_sum([1, 2, 3])
list_sum()  # 1
list_sum()  # 1
list_sum()  # 1

"""ключевые аргументы, можна заполнять в любом порядке"""
print(get_max_number(b=1, a=2, c=8))

def default_args2(*args, k, a):
    print(args, k, a)

default_args2(1, 2, 3, 5 ,6, 7, 4, k=2, a=4)

def default_args3(*args, **kwargs):  # * неограниченное количество позиционных аргументов
    print(args, kwargs)  # ** неограниченное количество ключевых аргументов

default_args3(1, 2, 3, 5 ,6, 7, 4, k=2, a=4)

x = 10

def global_view():
    global x # зміна значення глобаьної змінної
    x = 30
    print(x)

global_view()

def local_view():
    # print(f'local_view x = {x}')
    x = 20
    print(f'local_view x = {x}')
x = 15
print(f'global x = {x}')

local_view()
print(f'global x = {x}')
global_view()

"""Анотации - это указание типа данных для переменной, чтобы подсказать какой тип данных мы ожидаем"""

def annotations(a: int, b: int = 10) -> int:  # значение после ->  мы указываем тип данных результата
    print(f'A = {a} Type {type(a)}| B = {b} Type {type(a)}')
    return a * b
test = annotations('Hello world', 2)
print(test, type(test))
print(isinstance(1, int))  # функция проверяет являеться ли наш объект указанного типа данных
"""аннотация не изменяет тип, а просто уведомляет какого типа должно быть значение или результат"""
c = 4.5
print(isinstance(c, (int, float)))


"""Лямбда функции"""
# def foo(x: any):
#     return x + 1

"""Можно заменить эту функцию лямбда функцией - это одноразовые функции"""
foo = lambda a, b: a + b

numbers = [1, 2, 5, 4, 5, 7]
new_numbers = list(map(foo, numbers))
print(new_numbers)
numbers = [1, 2, 5, 4, 5, 7]
new_numbers = list(map(lambda x: -x, numbers))
print(new_numbers)











