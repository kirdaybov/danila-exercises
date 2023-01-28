d = {1: 'I', 2: 'II', 3: 'III' ,4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
number = int(input('Введите число от 1 до 10 \n'))
if 1<= number <= 10:
    print(f'{number}: {d[number]}')
else:
    print('Вы ввели число не из диапазона')