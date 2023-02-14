def separate_pb_from_number(number_table):
    pb_numbers = []
    for line in number_table:
        pb_numbers.append(int(line[-3:]))
    return pb_numbers

def separating_numbers(number_table):
    line_numbers = []
    for line in number_table:
        words = line.split()
        current_numbers = [int(word) for word in words[:5]]  #current - текущие числа
        line_numbers.append(current_numbers)
    return line_numbers

def most_ten_common_numbers(list_numbers):
    numbers_frequencies = [0] * 69
    for current_numbers in list_numbers:
        for number in current_numbers:
            numbers_frequencies[number] += 1
    ten_most_frequent_numbers = [] 
    for x in range(10):
        max_frequency = max(numbers_frequencies)
        most_frequent_number = numbers_frequencies.index(max_frequency)
        ten_most_frequent_numbers.append(most_frequent_number)
        numbers_frequencies[most_frequent_number] = 0
    return ten_most_frequent_numbers
        

def least_ten_common_numbers(list_numbers):
    numbers_frequencies = [0] * 69
    for current_numbers in list_numbers:
        for number in current_numbers:
            numbers_frequencies[number] += 1
    ten_least_frequent_numbers = [] 
    for x in range(10):
        least_frequency = max(numbers_frequencies)
        least_frequent_number = numbers_frequencies.index(least_frequency)
        ten_least_frequent_numbers.append(least_frequent_number)
        numbers_frequencies[least_frequent_number] = 0
    return ten_least_frequent_numbers

def purity_of_numbers(list_numbers):
    numbers_frequencies = [0] * 69
    for current_numbers in list_numbers:
        numbers_frequencies[current_numbers] += 1
    for x in range(69):
        print(f'Число {x} повторяется с частотой {numbers_frequencies[x]}')
        return numbers_frequencies

def purity_pbnumbers(pb_numbers):
    numbers_frequencies = [0] * 26
    for current_numbers in pb_numbers:
        numbers_frequencies[current_numbers] += 1
    for x in range(26):
        print(f'Число {x}(PB) повторяется с частотой {numbers_frequencies[x]}')  #КАК УБРАТЬ NONE?

def ripe_numbers(): #в эту функцию приходит результат от функции "purity_of_numbers" и всё первые 10 значений от минимального повторений выводятся
    pass
    

infile = open('pbnumbers.txt', 'r')

numbers = infile.readlines()

infile.close()

pb_numbers = separate_pb_from_number(numbers)
line_numbers = separating_numbers(numbers)





