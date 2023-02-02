credit = int(input('Введите месячный платеж за кредит:\n'))
insurance = int(input('Введите месячный платеж за страховку:\n'))
fuel = int(input('Введите месячный платеж за бензин:\n'))
machine_oil = int(input('Введите месячный платеж за машиное масло:\n'))
tires = int(input('Введите месячный платеж за резину:\n'))
maintenance = int(input('Введите месячный платеж за техобслуживание:\n'))

def calculate_monthly_cost(num1, num2, num3, num4, num5, num6):
    return num1 + num2 + num3 + num4 + num5 + num6

def calculate_year_cost(num1, num2, num3, num4, num5, num6):
    return (num1 + num2 + num3 + num4 + num5 + num6) * 12
    
monthly_cost = calculate_monthly_cost(credit, insurance, fuel, machine_oil, tires, maintenance)
year_cost = calculate_year_cost(credit, insurance, fuel, machine_oil, tires, maintenance)

print(f"Месячные расходы - {monthly_cost}\nГодовые расходы - {year_cost}")
