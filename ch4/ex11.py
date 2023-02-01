mass = float(input('Введите массу тела в кг:\n'))
mounth6 = 6
dietary_losses = 1.5

for mounth in range(1,mounth6 + 1):
    mass = mass - dietary_losses
    print(f'За {mounth} месяц диеты Вы начнёте весить {mass} кг')
