day = int(input('Введите кол-во дней:\n'))
salary_per_day = 0
salary_for_the_entire_period = 0

for copeyka in range(1,day + 1):
    salary_per_day = copeyka ** 2
    salary_for_the_entire_period = salary_for_the_entire_period + salary_per_day
    print(f'В {copeyka} день вы получите {salary_per_day}')
print (f'Всего Вы получите - {salary_for_the_entire_period}')