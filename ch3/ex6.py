month = int(input('Введите месяц в числовой форме: \n'))
day = int(input('Введите день в числовой форме: \n'))
year = int(input('Введите двузначный год в числовой форме: \n'))
magic_date = month * day
if magic_date == year:
    print('Данная дата магическая')
else:
    print('Данная дата не магическая')