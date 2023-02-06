MOUNTH = 12

rainfall = [0] * MOUNTH

print('Введите осадки за каждый месяц:\n')

for index in range(len(rainfall)):
    rainfall[index] = int(input(f'Месяц № {index + 1}: '))

def rainfall_year(rainfall_list):
    total = 0
    for num in rainfall_list:
        total = total + num
    return total

total_rainfall = rainfall_year(rainfall)

print(f'Общий объём осадков за год: {total_rainfall:.1f}')

def average_rainfall(rainfall_year):
    average = rainfall_year / MOUNTH
    return average

print(f'Среднее ежемесячное кол-во осадков: {average_rainfall(total_rainfall)}')

mounth_min_rainfall_index = (rainfall.index(min(rainfall))) 
mounth_min_rainfall = mounth_min_rainfall_index + 1

mounth_max_rainfall_index = (rainfall.index(max(rainfall))) 
mounth_max_rainfall = mounth_max_rainfall_index + 1

print('Месяц, в котором было минимальное кол-во осадков: ', mounth_min_rainfall)
print('Месяц, в котором было максимальное кол-во осадков: ', mounth_max_rainfall)
