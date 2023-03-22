import sqlite3

conn = sqlite3.connect('student_info.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Majors (MajorID INTEGER PRIMARY KEY NOT NULL,
                                    Name TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Departments (DeptID INTEGER PRIMARY KEY NOT NULL,
                                    Name TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Students (StudentID INTEGER PRIMARY KEY NOT NULL,
                                    StudentName TEXT,
                                    MajorID INTEGER,
                                    DeptID INTEGER,
                                    FOREIGN KEY (MajorID) REFERENCES
                                        Majors(MajorID),
                                    FOREIGN KEY (DeptID) REFERENCES
                                        Departments(DeptID))''')                                                         
conn.commit()
conn.close()

MIN_CHOICE = 1
MAX_CHOICE = 16
CREATE_MAJOR = 1
READ_MAJOR = 2
UPDATE_MAJOR = 3
DELETE_MAJOR = 4
SHOWALL_MAYOR = 5
CREATE_DEPT = 6
READ_DEPT = 7
UPDATE_DEPT = 8
DELETE_DEPT = 9
SHOWALL_DEPT = 10
CREATE_STUD = 11
READ_STUD = 12
UPDATE_STUD = 13
DELETE_STUD = 14
SHOWALL_STUD = 15
EXIT = 16

def display_menu():
    print('Меню работы с базой данных student_info')
    print('')
    print('1.Добавить новую специальность.')
    print('2.Отыскать существующую специальность.')
    print('3.Обновить существующую специальность..')
    print('4.Удалить существующую специальность.')
    print('5.Вывести список всех специальностей.')
    print('6.Добавить новый факультет.')
    print('7.Отыскать существующий факультет.')
    print('8.Обновить существующий факультет.')
    print('9.Удалить существующий факультет.')
    print('10.Вывести список всех факультетов.')
    print('11.Добавить нового студента.')
    print('12.Отыскать существующего студента.')
    print('13.Обновить существующего студента.')
    print('14.Удалить существующего студента.')
    print('15.Вывести список всех студентов.')
   
def get_menu_choice():
    choice = int(input('Введите ваш вариант:\n'))
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.')
        choice = int(input('Введите ваш вариант:\n'))
    return choice

def insert_student(name, major, department): #добавляеи строку в студентов
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute('''INSERT INTO Students 
                            (StudentName, MajorID, DeptID)
                        VALUES (?, ?, ?)''',
                            (name, major, department))
        conn.commit()
        print('Студент успешно добавлен!')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()

def display_students(): #выводит на экран всех студентов 
    conn = None
    results = []
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute('''SELECT
                            Students.StudentName
                            Departments.Name,
                            Majors.Name
                        FROM
                            Students, Departments, Majors
                        WHERE 
                            Students.DeptID == Departments.DeptID AND
                            Students.MajorID == Majors.MajorID''',
                        )
        results = cur.fetchall()

        for row in results:
            print(f'{row[0]:<3}  {row[1]:<15} {row[2]:<6}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return len(results)

def display_student(name): #выводит на экран все позиции с совпадающим студентом
    conn = None
    results = []
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Students
                        WHERE StudentName == ?''',
                        (name,))
        results = cur.fetchall()

        for row in results:
            print(f'ID: {row[0]:<3} Cтудент: {row[1]:<15} Специальность: {row[2]:<6} Факультет: {row[3]:<15}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return len(results)

def update_student(name,major, department, id): #обновляет существующую строку в студентах
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute('''UPDATE Students
                        SET StudentName = ?, MajorID = ?, DeptID = ?
                        WHERE StudentID == ?''',
                        (name,major, department,id))
        conn.commit()
        student_updated = cur.rowcount
        print('Студент успешно обновлен!')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return student_updated

def delete_student(id): #удаляет существующую позицию в студентах
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        cur.execute('''DELETE FROM Students
                        WHERE StudentID == ?''',
                        (id,))
        conn.commit()
        student_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return student_deleted

def create_student():
    print('Создать нового студента')
    name = input('Введите имя студента:\n')
    major = input('Введите специальность студента:\n')
    department = input('Введите факультет студента:\n')
    insert_student(name, major, department)

def read_student():
    name = input('Введите имя студента:\n')
    num_found = display_student(name)
    print(f'{num_found} строк(а) найдено.')

def update_student():
    read_student()
    selected_id = int(input('Выберете ID студента:\n'))
    name = input('Введите новое название позиции:\n')
    major = input('Введите новую специальность студента:\n')
    department = input('Введите новый факультет студента:\n')
    num_updated = update_student(selected_id, name, major, department)
    print(f'{num_updated} строк(а) обновлено.')

def delete_student():
    read_student()
    selected_id = int(input('Выберете ID удаляемой позиции:\n'))
    sure = input('Вы уверены, что хотите удалить эту позицию? (Y/N): \n')
    if sure.upper() == 'Y':
        num_deleted = delete_student(selected_id)
        print(f'{num_deleted} строк(а) удалено.')

def insert_major(name): #вставляет строку в специальности
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Majors (Name)
                        VALUES (?)''',
                        (name))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()

def display_majors(): #выводит на экран все специальности
    conn = None
    results = []
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Majors''')
        results = cur.fetchall()

        for row in results:
            print(f'Специальность ID: {row[0]:<3} Специальность: {row[1]:<15}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return len(results)

def display_major(name): #выводит на экран все позиции с совпадающими специальностями
    conn = None
    results = []
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Majors
                        WHERE ItemName == ?''',
                        (name,))
        results = cur.fetchall()

        for row in results:
            print(f'Специальность ID: {row[0]:<3} Специальность: {row[1]:<15}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return len(results)

def update_major(id, name): #обновляет существующую специальность
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Majors
                        SET Name = ?
                        WHERE MajorID == ?''',
                        (name,id))
        conn.commit()
        major_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return major_updated

def delete_major(id): #удаляет существующую специальность
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Majors
                        WHERE MajorID == ?''',
                        (id,))
        conn.commit()
        major_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return major_deleted

def create_major():
    print('Создать новую специальность')
    name = input('Введите название специальности:\n')
    insert_departments(name)

def read_major():
    name = input('Введите специальность:\n')
    major_found = display_major(name)
    print(f'{major_found} строк(а) найдено.')

def update_major_menu():
    read_major()
    selected_id = int(input('Выберете ID специальности:\n'))
    name = input('Введите новое название позиции:\n')
    major_updated = update_major(selected_id, name)
    print(f'{major_updated} строк(а) обновлено.')

def delete_major_menu():
    read_major()
    selected_id = int(input('Выберете ID удаляемой позиции:\n'))
    sure = input('Вы уверены, что хотите удалить эту позицию? (Y/N): \n')
    if sure.upper() == 'Y':
        major_deleted = delete_major(selected_id)
        print(f'{major_deleted} строк(а) удалено.')

def insert_department(name): #вставляет строку в факультеты
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Departments (Name)
                        VALUES (?)''',
                        (name))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()

def display_departments(): #выводит на экран все факультеты
    conn = None
    results = []
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Departments''')
        results = cur.fetchall()

        for row in results:
            print(f'Факультет ID: {row[0]:<3} Факультет: {row[1]:<15}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return len(results)

def display_department(name): #выводит на экран все позиции с совпадающими факультетами
    conn = None
    results = []
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Departments
                        WHERE ItemName == ?''',
                        (name,))
        results = cur.fetchall()

        for row in results:
            print(f'Факультет ID: {row[0]:<3} Факультет: {row[1]:<15}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return len(results)

def update_department(id, name): #обновляет существующий факультет
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Departments
                        SET Name = ?
                        WHERE DeptID == ?''',
                        (name,id))
        conn.commit()
        major_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return major_updated

def delete_department(id): #удаляет существующую специальность
    conn = None
    try:
        conn = sqlite3.connect('student_info.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Departments
                        WHERE DeptID == ?''',
                        (id,))
        conn.commit()
        major_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return major_deleted

def create_department():
    print('Создать новый факультет')
    name = input('Введите название факультета:\n')
    insert_departments(name)

def read_department():
    name = input('Введите факульет:\n')
    major_found = display_department(name)
    print(f'{major_found} строк(а) найдено.')

def update_department_menu():
    read_department()
    selected_id = int(input('Выберете ID факультета:\n'))
    name = input('Введите новое название позиции:\n')
    department_updated = update_department(selected_id, name)
    print(f'{department_updated} строк(а) обновлено.')

def delete_department_menu():
    read_department()
    selected_id = int(input('Выберете ID удаляемой позиции:\n'))
    sure = input('Вы уверены, что хотите удалить эту позицию? (Y/N): \n')
    if sure.upper() == 'Y':
        department_deleted = delete_department(selected_id)
        print(f'{department_deleted} строк(а) удалено.')

CHOICE = 0
while CHOICE != EXIT:
    display_menu()
    CHOICE = get_menu_choice()
    if CHOICE == CREATE_MAJOR:
        create_major()
    elif CHOICE == READ_MAJOR:
        read_major()
    elif CHOICE == UPDATE_MAJOR:
        update_major_menu()
    elif CHOICE == DELETE_MAJOR:
        delete_major_menu()
    elif CHOICE == SHOWALL_MAYOR:
        display_majors
    elif CHOICE == CREATE_DEPT:
        create_department()
    elif CHOICE == READ_DEPT:
        read_department()
    elif CHOICE == UPDATE_DEPT:
        update_department_menu()
    elif CHOICE == DELETE_DEPT:
        delete_department_menu()
    elif CHOICE == SHOWALL_DEPT:
        display_departments
    elif CHOICE == CREATE_STUD:
        create_student()
    elif CHOICE == READ_STUD:
        read_student()
    elif CHOICE == UPDATE_STUD:
        update_student()
    elif CHOICE == DELETE_STUD:
        delete_student()
    elif CHOICE == SHOWALL_STUD:
        display_students