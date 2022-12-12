from typing import Iterable, List, Tuple


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


seq1 = [1,    2, 3, 4, 5]
seq2 = [9,    8, 7]
seq3 = ['a', 'b']
seq4 = [0,    0, 0, 0]


assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
assert custom_zip(seq2, seq1) == [(9, 1), (8, 2), (7, 3)]

assert custom_zip(seq1, seq2, full=True) == [(1, 9), (2, 8), (3, 7), (4, None), (5, None)]
assert custom_zip(seq2, seq1, full=True) == [(9, 1), (8, 2), (7, 3), (None, 4), (None, 5)]

assert custom_zip(seq1, seq2, full=True, default="Q") == [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]  # FAIL is here
assert custom_zip(seq2, seq1, full=True, default="Q") == [(9, 1), (8, 2), (7, 3), ('Q', 4), ('Q', 5)]

assert custom_zip(seq1, seq2, seq3, full=True) == [(1, 9, 'a'), (2, 8, 'b'), (3, 7, None), (4, None, None), (5, None, None)]

assert custom_zip(seq1, seq2, seq3, seq4, full=True, default='Q') == [(1, 9, 'a', 0), (2, 8, 'b', 0), (3, 7, 'Q', 0), (4, 'Q', 'Q', 0), (5, 'Q', 'Q', 'Q')]
assert custom_zip(seq3, seq2, seq1, seq4, full=True, default='Q') == [('a', 9, 1, 0), ('b', 8, 2, 0), ('Q', 7, 3, 0), ('Q', 'Q', 4, 0), ('Q', 'Q', 5, 'Q')]



