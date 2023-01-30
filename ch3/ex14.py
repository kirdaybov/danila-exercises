mass = float(input('Введите масу тела в кг -\n'))
height = float(input('Введите рост в метрах-\n'))
body_mass_index = mass / (height**2) 
print ('Ваш ИМТ - ', body_mass_index)
if 18.5 <= body_mass_index <= 25:
    print('Ваша масса оптимальна')
elif body_mass_index < 18.5:
    print('Весите меньше нормы')
else: 
    print ('Весите больше нормы')