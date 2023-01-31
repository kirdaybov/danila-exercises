number_positive = int(input('Введите положительное число. Если хотите остановиться - введите отрицательное:\n'))
total_sum = 0

while number_positive > 0:
    total_sum += number_positive
    number_positive = int(input('Введите положительное число. Если хотите остановиться - введите отрицательное:\n'))
print(f'Сумма всех Ваших чисел - {total_sum}')