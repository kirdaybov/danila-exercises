BASE_SIZE = 7

for x in range(BASE_SIZE): #cколько строк
    for y in range(BASE_SIZE - x): #сколько столбцов
        print('*', end='')
    print()