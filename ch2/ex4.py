product_1 = int(input('Введите цену первого товара - '))
product_2 = int(input('Введите цену второго товара - '))
product_3 = int(input('Введите цену третьего товара - '))
product_4 = int(input('Введите цену четвёртого товара - '))
product_5 = int(input('Введите цену пятого товара - '))
sum = product_1 + product_2 + product_3 + product_4 + product_5
grand_total = sum * 0.7
tax_amount = sum - grand_total
print('накопленная стоимость товаров - ', sum)
print(' сумма налога с продаж - ', tax_amount)
print(' Итоговая сумма - ', grand_total)