from ex1 import Employee

class ShiftSupervisor(Employee):
    def __init__(self, name, ID, annual_salary, annual_bonus):
        Employee.__init__(self, name, ID)
        self.__annual_salary = annual_salary
        self.__annual_bonus = annual_bonus
    
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_bonus(self, annual_bonus):
        self.__annual_bonus = annual_bonus

    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_bonus(self):
        return self.__annual_bonus

    def __str__(self):
        result = 'Имя: ' + self.get_name() + '\n' + \
                 'ID: ' + self.get_ID() + '\n' + \
                 'Годовой оклад: ' + self.get_annual_salary() + '\n' + \
                 'Годовая премия: ' + self.get_annual_bonus()
        return result

name = input('Введите имя сотрудника:\n')
id = input('Введите ID сотрудника:\n')
annual_salary = input('Введите годовой оклад:\n')
annual_bonus = input('Введите годовую производственную премию:\n')

supervisor = ShiftSupervisor(name, id, annual_salary, annual_bonus)

print('Информация о начальнике смены:')
print(supervisor)

