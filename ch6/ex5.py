infile = open('numbers.txt', 'r')
sum = 0
number = 0
for line in infile:
    number = int(line)
    sum += number

print(sum)

infile.close()