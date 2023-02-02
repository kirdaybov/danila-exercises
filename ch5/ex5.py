price = int(input('Введите стоимость имущества:\n'))

def calculate_appraised_value(price):
    PERCENTAGE_OF_ASSESSED_VALUE = 0.6
    return price * PERCENTAGE_OF_ASSESSED_VALUE

def calculate_property_tax(appraised_value):
    TAX = 72
    return ((appraised_value / 100) * TAX) / 100

appraised_value = calculate_appraised_value(price)
property_tax = calculate_property_tax(appraised_value)

print(f'Оценочная стоимость равна - {appraised_value}\nНалог на имущество равен - {property_tax:.1f}')