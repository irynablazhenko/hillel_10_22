print(2 in [1, 2, 3, 4, 5, 6])
print(123 not in [1, 2, 3, 4, 5, 6])

print(2 in (1, 2, 3, 4, 5, 6))
print(123 not in (1, 2, 3, 4, 5, 6))  # tuple

print(2 in {1, 2, 3, 4, 5, 6})
print(123 not in {1, 2, 3, 4, 5, 6})  # dictionary

string = 'Hello world'
substring = 'w1'

print(substring in string)  # перевірка чи входить підстврока в строку
print(substring not in string)  # лише точне співпадіння

"""оператори тотожності"""
a = 4
b = 4
print(a is b)  # буде true, так як це ссилки на одне значення
print(a is not b)

print(-a)

print(True or False)  # true
print(False and True)  # false

"""оператори розгалуження"""
temp = 15

# if temp >= 40:
#     print('Too hot')
# elif temp >= 30:
#     print('hot')
# else:
#     # print(f'temperature: {temp}')
#     raise ValueError (f'{temp} в діапазоні до 30')  #

if ...:
    pass  # пропустити, нічого не робити
elif ...:
    pass
if ...:
    pass

"""відловлення помилки"""
try:                                    # блок перевірки на помилку. Суть: робимо дії, і якщо буде посилка ValueError - виводимо повідомлення зі змістом помилки.
    a = int(input('Enter number a: '))  # якщо помилку не прописати, то буде ловити будь які помилки
    b = int(input('Enter number b : '))
    if a == 10 and b > a:
        print('True')
    else:
        print("not True")
except ValueError as e:  # записує саму повідомлення про помилку у змінну е. Можна помилки прописувати декілька через кому в дужках (error1, error2)
    print(f'Error invalid number: {e}')
except ZeroDivisionError as e:
    print(f'Error division by zero: {e}')

a = int(input('Enter number a: '))

"""тернарний оператор"""
if a % 2 == 0:
    print('Tue')
else:
    print('not True')
print('True' if a % 2 == 0 else 'not True')

"""цикл"""
i = 0
while i < 5:
    print(f'i = {i}')
    i += 1

"""запросити у користувача число N, вивести всі числа від 0 до N які діляться на 3"""
N = int(input('Enter number N: '))
i=0
while i < N:
    if i % 3 == 0:
        print(i)
    i += 1

stop = True

N1, N2 = 1, 4  # або можна записати N1 = N2 = 1
while stop:
    symbol = input('Enter symbol: ')
    if symbol == 'q':
        stop = False
    print(N1 + N2)
    N1 += 1

while True:  # означає, що цикл ніколи не закінчиться
    symbol = input('Enter symbol: ')
    if symbol == 'q':
        break  # перериває цикл
    if N2 % 2 == 0:
        continue  # продовжує заново виконання циклу з початку. Після continue не виконається нічого, якщо умова виконується. continue пропускає ітерацію
    print(N1 + N2)

    N1 += 1

i=0
while i < N:
    i += 1
    if i % 3 == 0:
        print(i)
    if i == 10:
        break
else:  # виконується якщо цикл не був перерваний за допомогою break
    print('Done')

"""Цикл for"""
# for змінна in набор значень:
#     pass
for i in 1, 2, 3, 4, 5:  # кортеж
    print(f'i = {i}')

for i in 'Hello world':  # строка
    print(f'i = {i}')

# range(від, до, крок) - діапазон, якщо вказати просто range(10) - то поч значення 0 з кроком 1. Значення ДО - невключаючи
for i in range(100, 0, 5): # крок може бути мінусовим
    if i % 3 == 0:
        break
    if i % 2 == 0:
        continue
    print(i)

for _ in range(10):  # так можна написати якщо нам не важлива змінна і ми її н ебудемо більше використовувати
    print(f'Hello ', _)

