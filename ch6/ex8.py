infile = open('random numbers.txt', 'r')

count = 0
sum = 0
for line in infile:
    number = int(line)
    print(number)
    count += 1
    sum += number
    
print(f'Сумма чисел равна - {sum:.1f}\nКол-во случайных чисел - {count:.1f}')

infile.close()