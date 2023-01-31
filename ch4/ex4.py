speed = int(input('Введите скорость в км/ч:\n'))
time = int(input('Введите время в часах:\n'))

#distance = time * speed
print('Час\tПройденное расстояние')
print('------------------------------')

for x in range(1,time + 1):
    distance = x * speed
    print(f'{x}\t{distance}')