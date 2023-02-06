numbers = [1,2,3,4,5]

def sum_numbers(value_list):
    total = 0
    for num in value_list:
        total = total + num
    return total

print(f'Сумма составляет {sum_numbers(numbers)}')
