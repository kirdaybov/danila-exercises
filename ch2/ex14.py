initial_deposited_amount = float(input('Введите основную сумму, внесёную на счёт в самом начале\n'))
annual_interest_rate = float(input('Введите годовую процентную ставку, начисляемую на остаток счета\n'))
annual_interest_rate = annual_interest_rate / 100
frequency_of_interest_income_per_year = float(input('Введите частоту начисления процентного дохода в год\n'))
years_old_account = float(input('Введите кол-во лет сберегательного счёта\n'))
grand_total = initial_deposited_amount * ((1 + (annual_interest_rate / frequency_of_interest_income_per_year))**(frequency_of_interest_income_per_year * years_old_account))
print(f'Сумма денег, после заданного кол-во лет -{grand_total:.2f}')