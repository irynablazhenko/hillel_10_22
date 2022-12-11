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
    min_len = min(map(len, sequences))
    print(min_len)
    result_tuple = []
    i = 0
    j = 0
    summa = ()

    # result_tuple = sequences
    # print(f'result_tuple[0] {result_tuple[0]}')
    # a = ()
    # b = []
    # for i in range(min_len):
    #     a = result_tuple[0][i] + result_tuple[1][i]
    #     b.append(a)
    #     print(f'a {a}')
    # print(f'b {b}')

    # result_tuple = sequences
    # print(f'result_tuple[0] {result_tuple[0]}')
    # a = ()
    # b =[]
    # for i in range(min_len):
    #     a=0
    #     for j in range(2):
    #         a += result_tuple[j][i]
    #     b.append(a)
    #     print(f'a {a}')
    # print(f'b {b}')


    print(f'sequences {sequences}')
    lisst = list(map(tuple,sequences))
    print(f'sequences {lisst}')
    length = len(sequences)
    min_len = min(map(len, sequences))
    print(min_len)
    print(f'sequences {sequences}')
    i = 0
    a = tuple()
    b = tuple()

    for i in sequences:
        print(f'i {i}')
        for j, value in enumerate(i):
            a = sum(sequences[][j])

            print(f'a {a}')




    return result_tuple

zip_value = custom_zip(seq1, seq2, seq3)
# print(zip_value)
print(f'zip {list(zip(seq1, seq2, seq3))}')
