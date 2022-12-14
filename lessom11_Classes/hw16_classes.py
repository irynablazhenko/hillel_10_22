"""
Создать классы Employee (сотрудник) и Company (компания).
Классы должны содержать:
    минимум два поля экземпляров и одно поле класса
    минимум два метода экземпляра
    минимум один метод класса
    минимум один статический метод
К методам добавить строки документации.
Методы должные быть НЕ get/set поле, а что-то оригинальнее:) (но если надо их, тоже можно добавить)
Написать код который создает несколько экземпляров и взаимодействует с объектами
Задание в том числе и на фантазию
"""


# -------------------------------------------------------------------------------------------------
from Employee import *
from Company import *

"""Работа с класом сотрудников"""

"""Создание сотруников"""
andrew = Employee('Андрей', 'Козачок', 2, 900)
kostya = Employee('Костантин', 'Кривенко', 1, 500)
kristina = Employee('Кристина', 'Иванечко', 2, 1300)
"""Формирование списка из зп сотрудников"""
salaries = [andrew.salary, kostya.salary, kristina.salary]
"""Расчет зарплатного фонда"""
Employee.get_salary_total(salaries)
"""Расчет количества сотрудников при указанном приросте в %"""
Employee.employee_predict(0.4)
"""Создание сотруников"""
nikita = Employee('Никита', 'Петров', 4, 2700)
"""Добавление в список зп нового сотрудников"""
salaries.append(nikita.salary)
"""Расчет зарплатного фонда"""
Employee.get_salary_total(salaries)
"""Расчет количества сотрудников при указанном приросте в %"""
Employee.employee_predict(0.4)
"""Изменение имени"""
kristina.change_name('Крис')
"""Вывод инфо о сотруднике"""
kristina.print_employee_info()
"""Изменение фамилии"""
kostya.change_surname('Некравин')
"""Вывод инфо о сотруднике"""
kostya.print_employee_info()
"""Добавление информации о уровне англисйского"""
Employee.set_english_level('intermedia')
print(f'Уровень английского у {andrew.name} - {andrew.english_level}')

print('--------------------------------------------------------')
"""Работа с класом сотрудников"""
"""Создание компаний"""
netflix = Company('Netflix', 2009, 6.7, '1111-111-111', 2897)
colambia = Company('Colambia', 2000, 5, '2222-222-222', 4563)
pixel = Company('Pixel', 2010, 3, '3333-333-333', 544)
"""Вывод инфо о компании"""
netflix.print_conpany_info()
"""Изменение данных о компании"""
pixel.change_data('Pixel 2', 2014, 7, '3333-333-333', 1200)
"""Вывод инфо о компании"""
pixel.print_conpany_info()
"""Добавление описания компании"""
Company.set_description('Киностудии')
print(f'Описание компании {netflix.name} : {netflix.description}')

"""Расчет среднего рейта компаний"""
rates = [netflix.rate, colambia.rate, pixel.rate]
Company.get_rate_avg(rates)
"""Расчет среднего дохода компаний компаний"""
profit = [netflix.price, colambia.price, pixel.price]
Company.get_price_avg(profit)
"""Расчет ожидаемого дохода при приросте компаний на указанный %"""
Company.predict_amount(0.3, profit)
