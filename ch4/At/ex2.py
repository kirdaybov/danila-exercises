keep_going = 'Y'

while keep_going == 'Y':
    number1 = int(input('Введите первое число\n'))
    number2 = int(input('Введите второе число\n'))
    sum = number1 + number2
    print(f'Cумма равняется {sum}')
    keep_going = input('Если хотите вычеслить ещё один раз нажмите "Y"')