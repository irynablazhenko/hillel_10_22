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
    min_len = 0
    print(f'Список последовательностей - sequences: {sequences}')
    lens = list(map(len, sequences))
    m = min(lens)
    print(f'Длина каждой последовательности из всех последовательностей - lens: {lens}')
    print(f'Минимальная длина последовательности - m:  {m}')
    len_seq = len(sequences)
    print(f'Количество последовательностей - sequences - len_seq: {len_seq}')
    i = 0
    j = 0
    a = []
    tup = []
    for i in range(m):
        for j in sequences:
            a.append(j[i])
        print(f'a {a}')
        tup.append(tuple(a[len(a)-len_seq:]))
        print(f'tup {tup}')


    return tup

zip_value = custom_zip(seq1, seq2, seq3)
print(f'Результат выполнения custom_zip: \n\t{zip_value}')
print(f'zip {list(zip(seq1, seq2, seq3))}')

