cars = {
    'opel' : 50,
    'lada' : 10,
    'honda': 30,
}

car_make = input('Введите марку машины: \n')

if car_make.lower() in cars.keys():
    print('{} стоит {}'.format(car_make, cars[car_make.lower()]))
else:
    print(f'{car_make} не существует')