infile = open('numbers.txt', 'r')
count = 0
number = 0
sum = 0
for line in infile:
    number = int(line)
    count += 1
    sum += number

average = count / number
print(f'{average:.1f}')

infile.close()