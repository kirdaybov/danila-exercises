sugar = 1.5 / 48
butter = 1 / 48
flour = 2.75 / 48
number_of_rolls = int(input('Введите количество булок\n'))
print('Для', number_of_rolls, 'булок Вам понадобиться:')
print (f'Сахара - {sugar * number_of_rolls:.2f} Стакана(ов)')
print(f'Масла - {butter * number_of_rolls:.2f} Стакана(ов)')
print(f'Муки - {flour * number_of_rolls:.2f} Стакана(ов)')
#Тут есть мини баг, который я не знаю как пофиксить. Если округлять значение до 1-го символа - то округляется в большую сторону.
