try:
    infile = open('random numbers.txt', 'r')
    count = 0
    number = 0
    sum = 0
    for line in infile:
        number = int(line)
        count += 1
        sum += number
    

    average = sum / count
    print(f'{average:.1f}')

    infile.close()
except IOError:
    print('Произошла ошибка при прочтении файла')
except ValueError:
    print('Произошла ошибка конвертации типов')