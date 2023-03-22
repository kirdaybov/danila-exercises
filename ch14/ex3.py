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

