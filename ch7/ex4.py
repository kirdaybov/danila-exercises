NUMBERS = 20

number = [0] * NUMBERS

print('Введите числа:\n')

for index in range(len(number)):
    number[index] = int(input(f'Число № {index + 1}: '))

def sum_of_numbers(number_list):  #считаем сумму чисел в списке
    total = 0
    for num in number_list:
        total += num
    return total

sum_numbers = sum_of_numbers(number) #сумма чисел

def calculate_average(sum_numbers):  #считаем среднее арифметическое
    average = sum_numbers / NUMBERS
    return average

print(f'Минимальное число: {min(number)}')
print(f'Максимальное число: {max(number)}')
print(f'Сумма чисел: {sum_numbers}')
print(f'Среднее арифметическое: {calculate_average(sum_numbers)}')
