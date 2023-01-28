number_pocket = int(input('Введите кол-во пакетов - \n'))
price = 99
sum_pocket = number_pocket * 99

if 0 < number_pocket <= 9:
    print('Спасибо, что являетесь нашим клиентом, но хрен Вам, а не скидка')
elif 10 <= number_pocket <= 19:
    discount_amount = sum_pocket * 0.1
    total_price = sum_pocket - discount_amount
    print('Сумма Вашей скидки равна - ', discount_amount, '\nОбщая сумма после вычета скидки - ', total_price)
elif 20 <= number_pocket <= 49:
    discount_amount = sum_pocket * 0.2
    total_price = sum_pocket - discount_amount
    print('Сумма Вашей скидки равна - ', discount_amount, '\nОбщая сумма после вычета скидки - ', total_price)
elif 50 <= number_pocket <= 99:
    discount_amount = sum_pocket * 0.3
    total_price = sum_pocket - discount_amount
    print('Сумма Вашей скидки равна - ', discount_amount, '\nОбщая сумма после вычета скидки - ', total_price)
else:
    discount_amount = sum_pocket * 0.4
    total_price = sum_pocket - discount_amount
    print('Сумма Вашей скидки равна - ', discount_amount, '\nОбщая сумма после вычета скидки - ', total_price, '\nP.s: Вы наш любимый клиент')