class Employee:
    def __init__(self, name, id,  department, position):
        self.__name = name
        self.__id = id
        self.__department =  department
        self.__position = position
        
    def set_name(self, name):
        self.__name = name

    def set_id(self, id):
        self.__id = id

    def set_department(self, department):
        self.__department = department

    def set_position(self, position):
        self.__position = position

    def get_name(self):
        return self.__name 

    def get_id(self):
       return self.__id

    def get_department(self):
        return self.__department

    def get_position(self):
        return self.__position

    def __str__(self):
        return f'Имя: {self.__name}\n' + \
            f'Id: {self.__id}\n' + \
            f'Отдел: {self.__department}\n' + \
            f'Должность: {self.__position}'
    

employee_1 = Employee('Сьюзан Мейерс','47899','Бухгалтерия','Вице-президент')
employee_2 = Employee('Марк Джоунс','39119','IT','Программист')
employee_3 = Employee('Джой Роджерс','81774','Производственный','Инженер')



print('Информация по первому сотруднику')
print(employee_1)
print()
print('Информация по второму сотруднику')
print(employee_2)
print()
print('Информация по третьему сотруднику')
print(employee_3)
print()