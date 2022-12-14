class Employee:
    empAmount = 0

    def __init__(self, name, years, specialty, salary, ):
        self.name = name
        self.years = years
        self.specialty = specialty
        self.salary = salary
        Employee.empAmount += 1

    def show_emp_salary(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def show_emp_specialty(self):
        print("Name : ", self.name, ", Specialty: ", self.specialty)

    def show_overtime_bonus(self):
        print("Bonus amount for overtime: ", self.overtime_bonus)

    @classmethod
    def overtime_bonus(cls, overtime_bonus):
        cls.overtime_bonus = overtime_bonus

    @staticmethod
    def show_emp_amount():
        print("Total Employee %d" % Employee.empAmount)

    @staticmethod
    def assigned_task(specialty):
        if specialty == 'Dev':
            requirement = ['dev_task_1', 'dev_task_2', 'dev_task_3']
        elif specialty == 'QA':
            requirement = ['qa_task_1', 'qa_task_2']
        elif specialty == 'BA':
            requirement = ['ba_task_1', 'ba_task_3']
        else:
            requirement = ['other_task_1']
        return requirement


emp_Alex = Employee("Alex", 31, "Dev", 5000)
emp_Alex.show_emp_amount()
emp_Alex.show_emp_salary()
emp_Alex.show_emp_specialty()
print(emp_Alex.assigned_task("Dev"))
Employee.overtime_bonus(500)
Employee.show_emp_amount()
emp_Alex.show_overtime_bonus()