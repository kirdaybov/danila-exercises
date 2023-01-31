monthly_budget = float(input('Введите бюджет на месяц:\n'))
keep_going = "Y"
expenses = 0

while keep_going.upper() == 'Y':
    expenses_item = float(input('Введите статью расходов:\n'))
    expenses = expenses + expenses_item
    keep_going = input('Вы хотите ещё добавить расходы? Если да - введите "Y"\n')
total = monthly_budget - expenses
if total < 0:
    print(f'Вы в минусе на {total}')
else:
    print(f'Вы в плюсе на {total}')
