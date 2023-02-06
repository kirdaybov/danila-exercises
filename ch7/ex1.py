NUM_DAYS = 7

sales = [0] * NUM_DAYS

print('Введите продажи за каждый день:\n')

for index in range(len(sales)):
    sales[index] = float(input(f'День № {index + 1}: '))

print('Вот значения которые были введены:')

for value in sales:
    print(value)

def total_sales(sales_list):
    total = 0
    for num in sales_list:
        total = total + num
    return total

print(f'Общий объём продаж за неделю: {total_sales(sales)}')