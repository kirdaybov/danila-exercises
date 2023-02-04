infile = open('names.txt', 'r')
sum = 0
for line in infile:
    sum += 1

print(sum)

infile.close()