food_coust = int(input('Введите стоимость еды\n'))
tips = food_coust * 0.18
tax = food_coust * 0.07
print('Сумма чаевых с этой суммы - ', int(tips))
print('Сумма налога с этой суммы - ', int(tax))
print('Сумма надбавок с этой суммы - ', int(tips) + int(tax))
print('Итоговая сумма - ', food_coust + int(tips) + int(tax))
