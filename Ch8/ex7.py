infile = open('text.txt', 'r')

file = infile.readline()

infile.close()

uppercase = 0
lowercase = 0
number = 0
space = 0

for line in file:
    sumbol = str(line)
    if sumbol.isupper():
        uppercase += 1
    elif sumbol.islower():
        lowercase += 1
    elif sumbol.isdigit():
        number += 1
    elif sumbol.isspace():
        space += 1

print(line)

print(f'В вашем файле:\n{uppercase} - букв в верхнем регистре\n{lowercase} - букв в нижнем регистре\n{number} - цифр\n{space} - пробелов')
