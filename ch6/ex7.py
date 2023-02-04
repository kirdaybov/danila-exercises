import random

amount_number = int(input('Введите кол-во случайных чисел'))

infile = open('random numbers.txt', 'w')

for line in range(1,amount_number + 1):
    number = random.randint(1,500)
    infile.write(f'{number}\n')

infile.close()