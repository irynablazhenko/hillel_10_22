class Employee:
    department = 'QA engineer'
    count = 0  # счетчик сотрудников
    salaries = []

    def __init__(self, name, surname, work_experience, salary):
        """Инициализация эллементов класа"""
        self.name = name
        self.surname = surname
        self.work_experience = work_experience
        self.salary = salary
        self.english_level = 'intermedia'
        Employee.count += 1
        Employee.salaries.append(self.salary)

    def change_name(self, new_name):
        """Изменение имени сотрудника"""
        self.name = new_name
        print(f'Новое имя: {self.name}')

    def change_surname(self, new_surname):
        """Изменение фамилии сотрудника"""
        self.surname = new_surname
        print(f'Новая фамилия: {self.surname}')

    def change_english_level(self, new_english_level):
        """Изменение уровня английского сотрудника"""
        self.english_level = new_english_level
        print(f'Новый уровень английского: {self.english_level}')

    def print_employee_info(self):
        """Вывод информации о сотруднике"""
        print(
            f'Имя: {self.name},\nфамилия: {self.surname},\nстаж работы: {self.work_experience},\nзаработная плата: {self.salary},\nотдел: {Employee.department}\n')

    @staticmethod
    def get_salary_total(*salary: list):
        """Расчет зарплатного фонда"""
        summ = sum(salary[0])
        print(f'Зарплатный фонд: {summ}')
        return summ

    @classmethod
    def employee_predict(cls, increase):
        """Расчет количества сотрудников при указанном приросте в %"""
        count_employees = round(Employee.count * (increase + 1))
        print(
            f'Ожидаемый штат при приросте {increase} составит: {count_employees} человека, при текущем количестве {Employee.count} человек')
        return count_employees
