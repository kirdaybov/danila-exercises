mass_pocket = int(input('Введите массу пакета :\n'))
if 0 <= mass_pocket <= 200:
    cost = mass_pocket / 100 * 150
    print('Плата за доставку составит - ', cost)
elif 201 <= mass_pocket <= 600:
    cost = mass_pocket / 100 * 300
    print('Плата за доставку составит - ', cost)
elif 601 <= mass_pocket <= 1000:
    cost = mass_pocket / 100 * 400
    print('Плата за доставку составит - ', cost)
else:
    cost = mass_pocket / 100 * 475
    print('Плата за доставку составит - ', cost)    