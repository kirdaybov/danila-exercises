import random

is_finished = False
LOW = 1
HIGH = 100
win_number = random.randint(LOW, HIGH)

while not is_finished:
    s_number = input(f'Введите число от {LOW} до {HIGH}: ')
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
