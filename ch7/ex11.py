numbers = [[4,9,2],[3,5,7],[8,1,6]]

def LoShu(numbers):
    for row in numbers:
        for elements in row:
            print(elements)

def sum_of_numbers(number_list):  #считаем сумму чисел в списке
    total = 0
    for num in number_list:
        total += num
    return total

sum_of_numbers(numbers)