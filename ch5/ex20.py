import random

number = random.randint(1,100)
attempt = 0
num_user = int(input('Введите, какое число загадал комп:\n'))

while number != num_user:
    if number > num_user:
        print('Загаданное число больше')
        num_user = int(input('Попробуй ещё раз, введи новое число:\n'))
    if number < num_user:
        print('Загаданное число меньше')
        num_user = int(input('Попробуй ещё раз, введи новое число:\n'))
    attempt += 1
print(f"Молодец, ты угадал за {attempt} попыток. Это было число - {number}")    
