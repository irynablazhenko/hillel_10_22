"""
1. Написать функцию, которая возвращает слуайную строку заданной длины.
Строка должна состоять из больших и маленьких латинских букв и цифр.

def get_random_string(length: int) -> str:
  pass

Ограничения:
- Не использовать модуль string
- Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]
"""
# ______________________________________________________________________________________________________________
import random

while True:
    try:
        len_of_string = int(input('Введите длину строки: '))
        if len_of_string > 0:
            break
    except ValueError as e:
        print(f'Число не целое, ошибка: {e}')
print(f'Длина строки {len_of_string}')


def get_random_string(length: int) -> str:
    string = ''
    char_list = []
    while True:
        char_list.append(chr(random.randint(65, 90)))
        char_list.append(chr(random.randint(97, 122)))
        char_list.append(chr(random.randint(48, 57)))
        random_symbol = random.choice(char_list)
        string += random_symbol
        if len(string) == len_of_string:
            break
    return string


print(get_random_string(len_of_string))
