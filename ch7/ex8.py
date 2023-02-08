def search_in_names(list_names, search_name):
    if search_name in list_names:
        print(f' Имя: {search_name} популярное')
    else:
        print (f' Имя: {search_name} не популярное')

infile_girls = open('GirlNames.txt', 'r')
infile_boy = open('BoyNames.txt', 'r')

girls_names = infile_girls.readlines()
boys_names = infile_boy.readlines()

infile_girls.close()
infile_boy.close()

start = input('Если Вы хотите ввести имя мальчика, нажмите "M"\nЕсли Вы хотите ввести имя девочки, нажмите "W"\nЕсли Вы хотите ввести имя девочки и мальчика, нажмите "WM"\nЕсли хотите выйти из программы, нажмите любую другую букву')
if start.upper() == 'M':
    search_boy = input('Введите имя мальчика:\n')
    search_in_names(boys_names, search_boy)
elif start.upper() == 'W':
    search_girl = input('Введите имя девочки:\n')
    search_in_names(girls_names, search_girl)
elif start.upper() == 'WM' or start.upper() == 'MW':
    search_boy = input('Введите имя мальчика:\n')
    search_girl = input('Введите имя девочки:\n')
    search_in_names(boys_names, search_boy)
    search_in_names(girls_names, search_girl)
else:
    print('Праграмма закрывается')






