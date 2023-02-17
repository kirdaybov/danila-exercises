import pickle

inputfile = open ('adres.dat','rb')
adreses = pickle.load(inputfile)
inputfile.close()

def get_menu_choice():
    print('Имена и адреса')
    print('1.Отыскать нужный адрес')
    print('2.Добавить новое имя и адрес')
    print('3.Изменить существующий адрес')
    print('4.Удалить существующий адрес и имя')
    print('5.Выйти из программы')

    choice = int(input('Введите выбранный пункт\n'))

    while choice < LOOK_UP or choice > QUIT:
        print('Вы ввели недопустимое значение.')
        choice = int(input('Введите выбранный пункт\n'))
    return choice

def look_up(adreses):
    name = input ('Введите имя:\n')
    print(adreses.get(name, 'Не найдено.'))
    return adreses

def add(adreses):
    name = input ('Введите имя:\n')
    adres = input ('Введите адрес:\n')
    if name not in adreses:
        adreses[name] = adres
    else:
        print('Эта запись уже существует')
    return adreses

def change(adreses):
    name = input ('Введите имя:\n')
    if name in adreses:
        adres = input ('Введите адрес:\n')
        adreses[name] = adres
    else:
        print('Имя не найдено')
    return adreses

def delete(adreses):
    name = input ('Введите имя:\n')
    if name in adreses:
        del adreses[name]
    else:
        print("Имя не найдено")
    return adreses

#Глобальные константы для меню
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

adreses = {}

choice = 0

while choice != QUIT:
    choice = get_menu_choice()

    if choice == LOOK_UP:
        look_up(adreses)
    elif choice == ADD:
        add(adreses)
    elif choice == CHANGE:
        change(adreses)
    elif choice == DELETE:
        delete(adreses)
    
outputfile = open('adres.dat','wb')
pickle.dump(adreses, outputfile)
outputfile.close()

