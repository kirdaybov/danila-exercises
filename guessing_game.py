import random

is_finished = False
win_number = random.randint(1,100)

while not is_finished:
    s_number = input('Введите число от 1 до 100: ')
    if not s_number.isdigit():
        print('Вы ввели не число')
        continue
    number = int(s_number)
    if number > win_number:
        print('Меньше!')
    elif number < win_number:
        print('Больше!')
    else:
        is_finished = True
        print(f'Правильно, {win_number}!')
