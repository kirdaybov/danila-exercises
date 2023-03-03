NUMBERS = 20

def sum_of_numbers(number_list):  #считаем сумму чисел в списке
    total = 0
    for num in number_list:
        total += num
    return total

def calculate_average(number_list):  #считаем среднее арифметическое
    average = sum_of_numbers(number_list) / len(number_list) 
    return average

numbers = [0] * NUMBERS

print('Введите числа:\n')

for index in range(len(numbers)):
    numbers[index] = int(input(f'Число № {index + 1}: '))

sum_numbers = sum_of_numbers(numbers) #сумма чисел

print(f'Минимальное число: {min(numbers)}')
print(f'Максимальное число: {max(numbers)}')
print(f'Сумма чисел: {sum_numbers}')
print(f'Среднее арифметическое: {calculate_average(sum_numbers, NUMBERS)}')
