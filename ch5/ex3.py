minimum_percentage_of_insurance = 0.8

insurance_amount = int(input('Введите стоимость строения:\n'))

def min_insurance_amount(insurance_amount, minimum_percentage_of_insurance):
    print(f'Минимальная сумма страховки строения - {insurance_amount * minimum_percentage_of_insurance}')

min_insurance_amount(insurance_amount, minimum_percentage_of_insurance)