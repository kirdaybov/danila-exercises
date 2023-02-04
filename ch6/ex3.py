name_file = input('Введите имя файла:\n')

in_file = open(name_file, 'r')
counter = 0

for line in in_file:
    counter += 1
    line = line.rstrip('\n')
    print(f'{counter}: {line}')

in_file.close()