import random

number1 = random.randint(1,100)

number2 = random.randint(1,100)

number3 = number1 + number2

print (f'  {number1}\n+ {number2}')
user_answer = int(input("Введите правильный ответ на уравнение:\n"))

if user_answer == number3:
    print('Ты красавчик!')
else:
    print(f'Правильный ответ - {number3}, попробуй ещё раз')

