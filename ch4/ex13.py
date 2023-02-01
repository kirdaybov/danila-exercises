amount = int(input('Введите стартовое кол-во:\n'))
average_daily_increase = int(input('Введите среднесуточное увеличение в %:\n'))
day = int(input('Введите кол-во дней для размножения:\n'))

print('День\tПопуляция')
average_daily_increase /= 100

for x in range(1,day + 1):
    population = amount 
    population_increase = amount + (population * average_daily_increase)
    amount = population_increase
    print(f'{x}\t{population:.1f}')
