"""
Занятия проходят по понедельникам и четвергам в 19:15
Первое занятие произошло 17.10.2022. Всего 32 занятия.
Вывести список всех занятий в таком формате (номера лекций выровнены по правому краю):

Lecture  1: 17 Oct 2022
Lecture  2: 20 Oct 2022 19:15
...
Lecture  9: 14 Nov 2022 19:15
Lecture 10: 17 Nov 2022 19:15
...
Lecture 32: 02 Feb 2023 19:15
"""
# -------------------------------------------------------------------------------------------------
from datetime import timedelta, date

first_lesson = date(2022, 10, 17)

dates = []
next_lesson = first_lesson

lessons = []
dates.append(first_lesson)
for i in range(16):
    next_lesson += timedelta(days=3)
    dates.append(next_lesson)
    next1_lesson = next_lesson+timedelta(days=4)
    next_lesson = next1_lesson
    dates.append(next_lesson)
dates.pop()

print('Расписание занятий')
for i, value in enumerate(dates):
    print('Lecture '+'{:>3}'.format(i+1)+': {: %d %b %Y}'.format(dates[i])+' 19:15')