"""
3. Написать функцию, которая принимает несколько итерируемых объектов, и возвращает список из
кортежей составленных из элементов итерируемых объектов одного индекса.

Функция также должна принимать параметры с дефолтными значения:
full=False - по умолчанию "склеить" последовательности по кратчайшей, иначе по самой длинной
default=None - если full=True, вместо недостающих элементов поставить значение указанное в параметре default
seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
custom_zip(seq1, seq2) -> [(1, 9), (2, 8), (3, 7)]
custom_zip(seq1, seq2, full=True, default="Q") -> [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]

Встроенную функцию zip не используем.
def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
  pass
"""
# -------------------------------------------------------------------------------------------------------------
from typing import Iterable, List, Tuple

seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 4, 2, 0]
seq3 = [9, 4, 2, 6, 7, 3, 5]



def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
    print(f'Последовательности: {sequences}')
    len_sequences = len(sequences)  # Количество последовательностей
    i = 0
    j = 0
    items = []
    result_tuple = []
    if full:
        max_len = max(map(len, sequences))  # максимальная длина последовательности
        for i in range(len_sequences):
            while len(sequences[i]) < max_len:
                # расширение последовательностей до максимальной длины символами из default
                sequences[i].append(default)
        length = max_len
    else:
        length = min(list(map(len, sequences)))  # минимальная длина последовательности
    for i in range(length):
        for j in sequences:
            items.append(j[i])
        result_tuple.append(tuple(items[len(items) - len_sequences:]))

    return result_tuple


zip_value = custom_zip(seq1, seq2, seq3)
print(f'Результат выполнения custom_zip: \n\t{zip_value}')
print(f'zip {list(zip(seq1, seq2, seq3))}')
assert zip_value == list(zip(seq1, seq2, seq3))

zip_value_full = custom_zip(seq1, seq2, seq3, full=True, default=None)
print(f'Результат выполнения custom_zip с full=True: \n\t{zip_value_full}')
print(f'zip {list(zip(seq1, seq2, seq3))}')
assert zip_value_full == list(zip(seq1, seq2, seq3))
