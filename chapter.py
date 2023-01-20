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
#man = float(input('Сколько мужчин в группе\n'))
#woman = float(input('Сколько женщин в группе\n'))
#sum_people = man + woman
#procent_man = man / sum_people
#procent_woman = woman / sum_people
#print('Процент мужчин -', procent_man * 100, '%')
#print('Процент женщин -', procent_woman * 100, '%')

#git add .==> git commit -m """ ==> git push

#двенадцатая задача
#stock = 2000
#stock_purchase_price = 40
#share_sale_price = 42.75
# 0.03 - это не магическое число, а процент биржевому брокеру
#purchase_commission = (stock * stock_purchase_price) * 0.03
#sales_commission = (stock * share_sale_price) * 0.03
#sum_stock_purchase_price = stock * stock_purchase_price
#sum_share_sale_price = stock * share_sale_price
#purchase_amount = sum_stock_purchase_price + purchase_commission
#sale_amount = sum_share_sale_price + sales_commission
#total_amount = purchase_amount - (sum_share_sale_price + sales_commission)
#print('Это сколько Джо отдал за покупку акций -', sum_stock_purchase_price)
#print('Это сколько составила комисия брокоре при покупке -', purchase_commission)
#print('Это сколько всего Джо потратил на покупку -', purchase_amount )
#print('Это сумма, за которую Джо продал акции -', sum_share_sale_price)
#print('Это сумма комисси, при продаже - ', sales_commission)
#print('Это оставшаяся сумма у Джо, после всех махинаций - ', total_amount)
#if total_amount > 0:
#    print ('Джо оказался в плюсе на: ', total_amount)
#else:
#    print('Джо понес убытки в размере: ', total_amount) 

#тринадцатая задачка
#bed_length = float(input('Введите длину гряды в метрах\n'))
#size_of_space_in_meters = float(input('Введите пространство, занимаемое концевой опорой в метрах\n'))
#distance_between_grapes = float(input('Введите расстояние между виноградными лозами в метрах\n'))
#number_of_vines = (bed_length - (2 * size_of_space_in_meters)) / distance_between_grapes
#print('На гряде поместятся -', number_of_vines, 'лоз(а)')

#четырнадцатая задачка
initial_deposited_amount = float(input('Введите основную сумму, внесёную на счёт в самом начале\n'))
annual_interest_rate = float(input('Введите годовую процентную ставку, начисляемую на остаток счета\n'))
annual_interest_rate = annual_interest_rate / 100
frequency_of_interest_income_per_year = float(input('Введите частоту начисления процентного дохода в год\n'))
years_old_account = float(input('Введите кол-во лет сберегательного счёта\n'))
grand_total = initial_deposited_amount * ((1 + (annual_interest_rate / frequency_of_interest_income_per_year))**(frequency_of_interest_income_per_year * years_old_account))
print(f'Сумма денег, после заданного кол-во лет -{grand_total:.2f}')