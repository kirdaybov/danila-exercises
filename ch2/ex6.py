product = int(input('Введите величину покупки - '))
federal_tax = product * 0.05
regional_tax = product * 0.025
grand_total = product - (federal_tax + regional_tax)
print('Сумма покупки - ', product)
print('Федеральный налог равен - ', federal_tax)
print('Региональный налог равен - ', regional_tax)
print('Общий налог с продажи - ', federal_tax + regional_tax)
print("Общая сумма продажи - ", grand_total)
