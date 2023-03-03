from ex4 import Employee
import pickle

def load_employee():
    try:
        input_file = open(FILENAME, 'rb')
        employees_dct = pickle.load(input_file)
        input_file.close()
    except IOError:
        employees_dct = {}
    return employees_dct

def get_menu_choice():
    print('Меню')
    print('----------------------')
    print('1.Найти сотрудника')
    print('2.Добавить сотрудника')
    print('3.Изменить информацию о сотруднике')
    print('4.Удалить сотрудника')
    print('5.Выйти из программы')
    print()
    choice = int(input('Введите выбранный пункт:\n'))

    while choice < LOOKUP or choice > QUIT:
        choice = int(input('Вы ввели недопустимое значение, попробуйте снова\n'))
    return choice

def look_up(employees):
    name = input ("Введите имя:\n")
    print(employees.get(name,'Это имя не найденою'))

def add(employees):
    name = input ("Введите имя:\n")
    id = input ("Введите Id:\n")
    department = input ("Введите отдел:\n")
    position = input ("Введите должность:\n")

    entry = Employee(name, id, department, position)

    if name not in employees:
        employees[name] = entry
        print('Запись добавлена')
    else:
        print('Это имя уже существует')

def change(employees):
    name = input ("Введите имя:\n")
     
    if name in employees:
        id = input ("Введите новый Id:\n")
        department = input ("Введите новый отдел:\n")
        position = input ("Введите новую должность:\n")
        entry = Employee(name, id, department, position)
        employees[name] = entry
        print('Информация обновлена')
    else:
        print('Имя не найдено')

def delete(employees):
    name = input ("Введите имя:\n")

    if name in employees:
        del employees[name]
        print('Запись удалена')
    else:
        print('Имя не найдено')

def save_employees(employees):
    output_file = open(FILENAME, 'wb')
    pickle.dump(employees, output_file)
    output_file.close()

LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = 'employee.dat'

employees = load_employee()

choice = 0

while choice != QUIT:
    choice = get_menu_choice()

    if choice == LOOKUP:
        look_up(employees)
    elif choice == ADD:
        add(employees)
    elif choice == CHANGE:
        change(employees)
    elif choice == DELETE:
        delete(employees)

save_employees(employees)
