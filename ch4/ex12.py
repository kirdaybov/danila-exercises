number = int(input('Введите неотрицательное число:\n'))
factorial = 1

if number > 0:
    for x in range(1,number + 1):
        factorial *= x
    print(f'Факториал введеного Вами числа - {factorial}' )
else:
    print ('Вы ввели не то значение')