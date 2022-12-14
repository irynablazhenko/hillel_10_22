
class Employee:
    department = 'QA engineer'
    count = 0  # счетчик сотрудников

    """Инициализация эллементов класа"""

    def __init__(self, name, surname, work_experience, salary):
        self.name = name
        self.surname = surname
        self.work_experience = work_experience
        self.salary = salary
        Employee.count += 1

    """Изменение имени сотрудника"""

    def change_name(self, new_name):
        self.name = new_name
        print(f'Новое имя: {new_name}')

    """Изменение фамилии сотрудника"""

    def change_surname(self, new_surname):
        self.surname = new_surname
        print(f'Новая фамилия: {new_surname}')

    """Вывод информации о сотруднике"""

    def print_employee_info(self):
        print(
            f'Имя: {self.name},\nфамилия: {self.surname},\nстаж работы: {self.work_experience},\nзаработная плата: {self.salary},\nотдел: {Employee.department}\n')

    """Расчет зарплатного фонда"""

    @staticmethod
    def get_salary_total(*salary: list):
        summ = sum(salary[0])
        print(f'Зарплатный фонд: {summ}')
        return summ

    """Опциональное поле - уровень английского сотрудника"""

    @classmethod
    def set_english_level(cls, english_level):
        cls.english_level = english_level

    """Расчет количества сотрудников при указанном приросте в %"""

    @classmethod
    def employee_predict(cls, increase):
        count_employees = round(Employee.count * (increase + 1))
        print(
            f'Ожидаемый штат при приросте {increase} составит: {count_employees} человека, при текущем количестве {Employee.count} человек')
        return count_employees