year = int(input('Введите кол-во лет:\n'))
total_month = 0
total_precipitation = 0

for x in range(1,year + 1):
    for month in range(1,13):
        precipitation = float(input(f'Введите кол-во осадков в {month}-ом месяце:\n'))
        total_month += 1
        total_precipitation = total_precipitation + precipitation
    average_thickness = total_precipitation / total_month
print(f'Кол-во месяцев - {total_month}\nКол-во миллиметров осадков - {total_precipitation}\nСредняя толщина слоя дождевых осадков - {average_thickness:.1f}')