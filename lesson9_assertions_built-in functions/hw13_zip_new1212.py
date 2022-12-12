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
seq2 = [9, 8, 7]
seq3 = ['a', 'b']
seq4 = [0, 0, 0, 0]


def custom_zip(*sequences: Iterable, full=False, default=None) -> List[Tuple]:
    # print(f'Последовательности: {sequences}')
    items = []
    result_tuple = []
    new_sequences = []
    """клонирование всех контейнеров sequences"""
    for seq in sequences:
        intermediate_array = []
        j = 0
        while j < len(seq):
            intermediate_array.append(seq[j])
            j += 1
        new_sequences.append(intermediate_array)

    tuple_seq = tuple(new_sequences)
    len_tuple_sequences = len(tuple_seq)  # Количество последовательностей
    i = 0
    if full:
        max_len = max(map(len, tuple_seq))  # максимальная длина последовательности
        if default is None:
            def_value = None
        else:
            def_value = default

        for i in range(len_tuple_sequences):

            while len(tuple_seq[i]) < max_len:
                # расширение последовательностей до максимальной длины символами из default
                tuple_seq[i].append(def_value)
        length = max_len

    else:
        length = min(list(map(len, tuple_seq)))  # минимальная длина последовательности
    j = 0
    for i in range(length):
        for j in tuple_seq:
            items.append(j[i])
        result_tuple.append(tuple(items[len(items) - len_tuple_sequences:]))

    return result_tuple


zip_value = custom_zip(seq1, seq2, seq3)
print(f'Результат выполнения custom_zip: \n\t{zip_value}')
print(f'zip {list(zip(seq1, seq2, seq3))}')
assert zip_value == list(zip(seq1, seq2, seq3))

zip_value_full = custom_zip(seq1, seq2, seq3, full=True, default=None)
print(f'Результат выполнения custom_zip с full=True: \n\t{zip_value_full}')
print(f'zip {list(zip(seq1, seq2, seq3))}')


assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
assert custom_zip(seq2, seq1) == [(9, 1), (8, 2), (7, 3)]

assert custom_zip(seq1, seq2, full=True) == [(1, 9), (2, 8), (3, 7), (4, None), (5, None)]
assert custom_zip(seq2, seq1, full=True) == [(9, 1), (8, 2), (7, 3), (None, 4), (None, 5)]

assert custom_zip(seq1, seq2, full=True, default="Q") == [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]  # FAIL is here
assert custom_zip(seq2, seq1, full=True, default="Q") == [(9, 1), (8, 2), (7, 3), ('Q', 4), ('Q', 5)]

assert custom_zip(seq1, seq2, seq3, full=True) == [(1, 9, 'a'), (2, 8, 'b'), (3, 7, None), (4, None, None), (5, None, None)]

assert custom_zip(seq1, seq2, seq3, seq4, full=True, default='Q') == [(1, 9, 'a', 0), (2, 8, 'b', 0), (3, 7, 'Q', 0), (4, 'Q', 'Q', 0), (5, 'Q', 'Q', 'Q')]
assert custom_zip(seq3, seq2, seq1, seq4, full=True, default='Q') == [('a', 9, 1, 0), ('b', 8, 2, 0), ('Q', 7, 3, 0), ('Q', 'Q', 4, 0), ('Q', 'Q', 5, 'Q')]



