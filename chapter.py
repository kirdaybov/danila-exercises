#product_1 = int(input('Введите цену первого товара - '))
#product_2 = int(input('Введите цену второго товара - '))
#product_3 = int(input('Введите цену третьего товара - '))
#product_4 = int(input('Введите цену четвёртого товара - '))
#product_5 = int(input('Введите цену пятого товара - '))
#sum = product_1 + product_2 + product_3 + product_4 + product_5
#grand_total = sum * 0.7
#tax_amount = sum - grand_total
#print('накопленная стоимость товаров - ', sum)
#print(' сумма налога с продаж - ', tax_amount)
#print(' Итоговая сумма - ', grand_total)
# четвёртая задачка

#пятая задачка
#distance = speed * time
#speed = 70
#distance_6hours = speed * 6
#distance_10hours = speed * 10
#distance_15hours = speed * 15
#print('Расстояние пройдённое за 6 часов - ', distance_6hours)
#print('Расстояние пройдённое за 10 часов - ', distance_10hours)
#print('Расстояние пройдённое за 15 часов - ', distance_15hours)

#шестая задачка
#product = int(input('Введите величину покупки - '))
#federal_tax = product * 0.05
#regional_tax = product * 0.025
#grand_total = product - (federal_tax + regional_tax)
#print('Сумма покупки - ', product)
#print('Федеральный налог равен - ', federal_tax)
#print('Региональный налог равен - ', regional_tax)
#print('Общий налог с продажи - ', federal_tax + regional_tax)
#print("Общая сумма продажи - ", grand_total)

#седьмая задачка
#gasoline_consumption = kilometers_traveled // gasoline_consumption_in_letres
#kilometers_traveled = int(input("Введите пройденное расстояние - "))
#gasoline_consumption_in_letres = int(input("Введите расход бензина - "))
#gasoline_consumption = kilometers_traveled // gasoline_consumption_in_letres
#print(' Расход бензина автомобилем - ', gasoline_consumption)

#восьмая задачка
#food_coust = int(input('Введите стоимость еды\n'))
#tips = food_coust * 0.18
#tax = food_coust * 0.07
#print('Сумма чаевых с этой суммы - ', int(tips))
#print('Сумма налога с этой суммы - ', int(tax))
#print('Сумма надбавок с этой суммы - ', int(tips) + int(tax))
#print('Итоговая сумма - ', food_coust + int(tips) + int(tax))

#девятая задачка
#degrees_Celsius = int(input('Введите градусы Цельсия\n'))
#degrees_Farengeite = 9 * degrees_Celsius // 5 + 32
#print("В Фаренгейтах это - ", degrees_Farengeite)

#Десятая задачка
#sugar = 1.5 / 48
#butter = 1 / 48
#flour = 2.75 / 48
#number_of_rolls = int(input('Введите количество булок\n'))
#print('Для', number_of_rolls, 'булок Вам понадобиться:')
#print (f'Сахара - {sugar * number_of_rolls:.2f} Стакана(ов)')
#print(f'Масла - {butter * number_of_rolls:.2f} Стакана(ов)')
#print(f'Муки - {flour * number_of_rolls:.2f} Стакана(ов)')
#Тут есть мини баг, который я не знаю как пофиксить. Если округлять значение до 1-го символа - то округляется в большую сторону.

#одиннадцатая задача
man = float(input('Сколько мужчин в группе\n'))
woman = float(input('Сколько женщин в группе\n'))
sum_people = man + woman
procent_man = man / sum_people
procent_woman = woman / sum_people
print('Процент мужчин -', procent_man * 100, '%')
print('Процент женщин -', procent_woman * 100, '%')