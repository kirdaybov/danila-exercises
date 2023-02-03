current_account_balance = float(input('Введите текущую сумму на счёте:\n'))
monthly_interest_rate = float(input('Введите ежемесячную процентную ставку:\n'))
number_of_months = float(input('Введите кол-во месяцев, сколько деньги будут лежать на счёте:\n'))

def caclulate_future_amount(current_account_balance, monthly_interest_rate, number_of_months):
    future_amount = current_account_balance * (1 + monthly_interest_rate) ** number_of_months
    print(f'Будущая сумма - {future_amount}')

caclulate_future_amount(current_account_balance, monthly_interest_rate, number_of_months)