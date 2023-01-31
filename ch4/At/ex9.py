number = int(input('Введите число от 1 до 100\n'))

while number < 1 or number > 100:
    print('Вы ввели недопустимое значение')
    number = int(input('Введите число от 1 до 100\n'))
