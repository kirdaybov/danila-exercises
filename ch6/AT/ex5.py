infile = open('number_list.txt', 'r')
sum = 0
for line in infile:
    amount = int(line)
    sum += amount

print(sum)

infile.close()