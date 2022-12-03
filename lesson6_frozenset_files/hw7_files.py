"""
Задание 1
Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers

Задание 2
Запросить у пользователя текст и записать его в файл data_task1.txt

Задание 3
Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел

Задание 4
Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число

Задание 5
Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю

Задание 6
Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

Задание 7
Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
'в' - 20 раз
'привет' - 10 раз
'как' - 9 раз
'у' - 7
'world' - 4
"""
# ____________________________________________________________________________________________________________
"""Задание 1
Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers"""
print('Задание 1')
data_from_file = open('../utils/data.txt', 'r', encoding='UTF-8')
f_list = data_from_file.readlines()
data_from_file.close()

"""Преобразование данных из файла с список слов"""
i = 0
lines = []
words_from_lines = []
symbols = ['\n', '.', '-', '_', '?', '!', '"', "'", ':', ';', '[', ']', '{', '}', '(', ')', '@', '#', '$', '%', '^', '&', '*', '№', '+', '=', '/', '<', '>', '|', '«', '»', '—', ',']
for _ in f_list:
    string = f_list[i]
    for l in symbols:
        if string.find(l)>0:
            string = string.replace(l, "")
            str = string
        else:
            str = string
    lines.append(str)
    words_from_lines += lines[i].split(' ')
    i += 1

"""Подсчет количества чисел в тексте и вывод списка этих чисел"""
numbers = []
count = 0
for i in words_from_lines:
    try:
        numbers.append(int(i))
        if i.isdigit():
            count += 1
        else:
            pass
    except ValueError as e:
        continue
print(f'Количество целых чисел в тексте: {count}. Список чисел из текста: {numbers}')
# ____________________________________________________________________________________________________________
"""Задание 2
Запросить у пользователя текст и записать его в файл data_task1.txt"""
print('\nЗадание 2')
text = input('Введите текст: ')
file = open('../utils/data_task1', 'w', encoding='UTF-8')
file.write(text)
# ____________________________________________________________________________________________________________
"""Задание 3
Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел"""
print('\nЗадание 3')
"""Валидация ввода числа N"""
while True:
    try:
        N = int(input('Введите количество чисел - целое число больше 0: '))
        if N > 0:
            break
        else:
            print(f'Число {N} не больше 0, повторите попытку')
    except ValueError as e:
        print(f'Вы ввели не целое число, ошибка: {e}')
        continue

file_of_numbers = open('../utils/numbers.txt', 'w', encoding='UTF-8')
i = 1
while i <= N:
    try:
        numbers = int(input(f'Введите целое {i}-e число: '))
        file_of_numbers.write(f'{numbers} ')
        i += 1
    except ValueError as e:
        print(f'Вы ввели не число. Ошибка: {e}')
file_of_numbers.close()
# ____________________________________________________________________________________________________________
"""Задание 4
Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число"""
print('\nЗадание 4')

import random

random_numbers = [random.randint(1, 1000) for _ in range(100)]
file_random_numbers = open('../utils/random_numbers.txt', 'w', encoding='UTF-8')
for i in random_numbers:
    file_random_numbers.write(f'{i} ')
print('Рандомні числа записані у файлі random_numbers.txt')
# ____________________________________________________________________________________________________________
"""Задание 5
Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю"""
print('\nЗадание 5')
file = open('../utils/data.txt', 'r', encoding='UTF-8')
file_data = file.readlines()
file.close()

"""Преобразование данных из файла с список слов"""
i = 0
lines = []
list_of_words = []
for _ in file_data:
    string = file_data[i]
    for l in symbols:
        if string.find(l) > 0:
            string = string.replace(l, "")
            new_string = string
        else:
            new_string = string
    lines.append(new_string)
    list_of_words += lines[i].split(' ')
    i += 1

"""Подсчет количества слов в тексте"""
i = 0
words = []
count = 0
for i in list_of_words:
    if i.isalpha():
        words.append(i)
        count += 1
    # else:
    #     pass
print(f'Количество слов в тексте: {count}.')
# ____________________________________________________________________________________________________________
"""Задание 6
Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел"""
print('\nЗадание 6')
file = open('../utils/task6_numbers.txt', 'r', encoding='UTF-8')
file_data = file.read()
print(f'Числа из файла: {file_data}')
file.close()
numbers = file_data.split(' ')
summa = sum(map(float, numbers))
print(f'Сумма чисел из  файла равна: {summa}')
# ____________________________________________________________________________________________________________
"""Задание 7
Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
'в' - 20 раз
'привет' - 10 раз
'как' - 9 раз
'у' - 7
'world' - 4"""
print('\nЗадание 7')
text_from_file = open('../utils/task7_text.txt', 'r', encoding='UTF-8')
file_data = text_from_file.readlines()
# print(f'текст из файла: {file_data}')
text_from_file.close()

import collections

"""Преобразование текста в список без знаков препинания и спец символов"""
i = 0
lines = []
list_of_words = []
for _ in file_data:
    string = file_data[i]
    for s in symbols:
        if string.find(s) > 0:
            string = string.replace(s, "")
            new_string = string
        else:
            new_string = string

    lines.append(new_string.lower())  # игнорирование заглавных букв
    list_of_words += lines[i].split(' ')
    i += 1

counter = collections.Counter(list_of_words).most_common(5)
print(f'Топ 5 строк которые чаще всего повторяются')
for i in range(len(counter)):
    print(f"Повторения слова '{counter[i][0]}' - {counter[i][1]} раз")



