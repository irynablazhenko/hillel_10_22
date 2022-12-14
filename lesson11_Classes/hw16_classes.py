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
employees = [andrew, kostya, kristina]

"""Расчет зарплатного фонда"""
Employee.get_salary_total(Employee.salaries)

"""Расчет количества сотрудников при указанном приросте в %"""
Employee.employee_predict(0.4)

"""Создание сотруников"""
nikita = Employee('Никита', 'Петров', 4, 2240)
employees.append(nikita)

"""Расчет зарплатного фонда с учетом нового сотрудника"""
Employee.get_salary_total(Employee.salaries)

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

"""Смена уровня английского"""
kristina.change_english_level('upper')
kristina.print_employee_info()


print('--------------------------------------------------------')

"""Работа с класом сотрудников"""
"""Создание компаний"""
netflix = Company('Netflix', 2009, 6.7, '1111-111-111', 2897)
colambia = Company('Colambia', 2000, 5, '2222-222-222', 4563)
pixel = Company('Pixel', 2010, 3, '3333-333-333', 544)
companies = [netflix, colambia, pixel]
rates = [company.rate for company in companies]

"""Вывод инфо о компании"""
netflix.print_conpany_info()

"""Вывод инфо о компании"""
pixel.print_conpany_info()

"""Расчет среднего рейта компаний"""
Company.get_rate_avg(rates)

"""Расчет среднего дохода компаний компаний"""
profit = [company.price for company in companies]
Company.get_price_avg(profit)

"""Расчет ожидаемого дохода при приросте компаний на указанный %"""
Company.predict_amount(0.3, profit)


"""Изменение данных о компании"""
pixel.print_conpany_info()  # печать данные до изменения
pixel.change_data({'name': 'Pixel 5', 'price': 342})
pixel.print_conpany_info()
