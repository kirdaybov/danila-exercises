year = int(input('Введите год - '))
if year % 100 == 0 and year % 400 == 0:
    print(year, ' - високосный год')
elif year % 100 != 0 and year % 4 == 0:
    print(year, ' - високосный год')
else:
    print('год не високосный')