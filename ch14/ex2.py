import sqlite3

conn = sqlite3.connect('phonebook.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Entries (ItemID INTEGER PRIMARY KEY NOT NULL,
                                    ItemName TEXT,
                                    Number INTEGER)''')
conn.commit()
conn.close()

MIN_CHOICE = 1
MAX_CHOICE = 5
CREATE = 1
READ = 2
UPDATE = 3
DELETE = 4
EXIT = 5

def display_menu():
    print('Меню работы с номерами людей')
    print('1.Создать новый контакт.')
    print('2.Найти контакт.')
    print('3.Изменить контакт.')
    print('4.Удалить контакт.')
    
def get_menu_choice():
    choice = int(input('Введите ваш вариант:\n'))
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.')
        choice = int(input('Введите ваш вариант:\n'))
    return choice

def insert_row(name, number): #вставляет строку
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''INSERT INTO Entries (ItemName, Number)
                        VALUES (?, ?)''',
                        (name, number))
        conn.commit()
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()

def display_item(name): #выводит на экран все позиции с совпадающими названиями
    conn = None
    results = []
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM Entries
                        WHERE ItemName == ?''',
                        (name,))
        results = cur.fetchall()

        for row in results:
            print(f'ID: {row[0]:<3} Имя: {row[1]:<15} Номер: {row[2]:<6}')
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return len(results)

def update_row(id, name, number): #обновляет существующую строку
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''UPDATE Entries
                        SET ItemName = ?, Number = ?
                        WHERE ItemID == ?''',
                        (name,number,id))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return num_updated

def delete_row(id): #удаляет существующую позицию
    conn = None
    try:
        conn = sqlite3.connect('phonebook.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM Entries
                        WHERE ItemID == ?''',
                        (id,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Ошибка базы данных', err)
    finally:
        if conn != None:
            conn.close()
        return num_deleted


def create():
    print('Создать новую позицию')
    name = input('Введите имя человека:\n')
    number = int(input('Введите номер человека:\n'))
    insert_row(name, number)

def read():
    name = input('Введите имя человека:\n')
    num_found = display_item(name)
    print(f'{num_found} строк(а) найдено.')

def update():
    read()
    selected_id = int(input('Выберете ID человека:\n'))
    name = input('Введите новое название позиции:\n')
    number = int(input('Введите новый номер:\n'))
    num_updated = update_row(selected_id, name, number)
    print(f'{num_updated} строк(а) обновлено.')

def delete():
    read()
    selected_id = int(input('Выберете ID удаляемой позиции:\n'))
    sure = input('Вы уверены, что хотите удалить эту позицию? (Y/N): \n')
    if sure.upper() == 'Y':
        num_deleted = delete_row(selected_id)
        print(f'{num_deleted} строк(а) удалено.')

CHOICE = 0
while CHOICE != EXIT:
    display_menu()
    CHOICE = get_menu_choice()
    if CHOICE == CREATE:
        create()
    elif CHOICE == READ:
        read()
    elif CHOICE == UPDATE:
        update()
    elif CHOICE == DELETE:
        delete()
