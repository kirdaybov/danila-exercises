import sqlite3

MIN_CHOICE = 1
MAX_CHOICE = 8
ASCENDING_POP = 1
DESCENDING_POP = 2
SORT_NAME = 3
TOTAL_POP = 4
AVERAGE_POP = 5
MAX_POP = 6
MIN_POP =7
EXIT = 8

def display_menu():
    print('Меню работы с городами из базы данных cities.db')
    print('1.Отсортировать по численности населения в порядке возрастания.')
    print('2.Отсортированных по численности населения в порядке убывания.')
    print('3.Отсортированных по названию городов.')
    print('4.Высчитать общую численность населения городов.')
    print('5.Высчитать среднюю численность населения городов.')
    print('6.Показать город с наибольшей численностью населения.')
    print('7.Показать город с наименьшей численностью населения.')
    print('8.Выйти из программы.')

def get_menu_choice():
    choice = int(input('Введите ваш вариант:\n'))
    while choice < MIN_CHOICE or choice > MAX_CHOICE:
        print(f'Допустимые варианты таковы: {MIN_CHOICE} - {MAX_CHOICE}.')
        choice = int(input('Введите ваш вариант:\n'))
    return choice
            
def ascending_population(cur): #Для вывода городов, отсортированных по численности населения в порядке возрастания
    print('Список городов, отсортированных по численности населения в порядке возрастания базы данных cities.db:')
    cur.execute('''SELECT CityName, Population FROM Cities ORDER BY Population''')
    result = cur.fetchall()
    for row in result:
        print(f'{row[0]:20}{row[1]:,.0f}')

def descending_population(cur): #Для вывода городов, отсортированных по численности населения в порядке убывания
    print('Список городов, отсортированных по численности населения в порядке убывания базы данных cities.db:')
    cur.execute('''SELECT CityName, Population FROM Cities ORDER BY Population DESC''')
    result = cur.fetchall()
    for row in result:
        print(f'{row[0]:20}{row[1]:,.0f}')

def sort_by_name(cur): #Для вывода городов, отсортированных по названию
    print('Список городов, отсортированных по названию базы данных cities.db:')
    cur.execute('''SELECT CityName FROM Cities ORDER BY CityName''')
    result = cur.fetchall()
    for row in result:
        print(f'{row[0]}')

def total_population(cur):
    print('Общая численность населения городов базы данных cities.db:')
    cur.execute('''SELECT SUM(Population) FROM Cities''')
    result = cur.fetchall()
    for row in result:
        print(f'{int(row[0])} человек')

def average_population(cur):
    print('Средняя численность населения городов базы данных cities.db:')
    cur.execute('''SELECT AVG(Population) FROM Cities''')
    result = cur.fetchall()
    for row in result:
        print(f'{int(row[0])} человек')

def maximum_population(cur):
    print('Город с наибольшей численностью населения из базы данных cities.db:')
    cur.execute('''SELECT CityName, MAX(Population) FROM Cities''')
    result = cur.fetchall()
    for row in result:
        print(f'{row[0]:20}{row[1]:,.0f}')

def minimum_population(cur):
    print('Город с наименьшей численностью населения из базы данных cities.db:')
    cur.execute('''SELECT CityName, MIN(Population) FROM Cities''')
    result = cur.fetchall()
    for row in result:
        print(f'{row[0]:20}{row[1]:,.0f}')

conn = sqlite3.connect('cities.db')
cur = conn.cursor()

CHOICE = 0

while CHOICE !=EXIT:
    display_menu()
    CHOICE = get_menu_choice()
    if CHOICE == ASCENDING_POP:
        ascending_population(cur)
    elif CHOICE == DESCENDING_POP:
        descending_population(cur)
    elif CHOICE == SORT_NAME:
        sort_by_name(cur)
    elif CHOICE == TOTAL_POP:
        total_population(cur)
    elif CHOICE == AVERAGE_POP:
        average_population(cur)
    elif CHOICE == MAX_POP:
        maximum_population(cur)
    elif CHOICE == MIN_POP:
        minimum_population(cur)

conn.commit()
conn.close()