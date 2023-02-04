name_file = input('Введите название файла:\n')

TOTAL = 5

file = open(name_file,'r')
index = 0
for line in file.readlines():
    index += 1
    print(line)
    if index >= TOTAL:
        break

file.close()

# break - выход из цикла
# continue - переход на следующую итерацию цикла