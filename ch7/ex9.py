def sum_of_popution(populition_list):  #считаем популяцию за всё время
    total = 0
    for num in populition_list:
        total += num
    return total

def calculate_average_annual_change(populition_list):  #считаем среднегодовое изменение
    average = sum_of_popution(populition_list) / len(populition_list) 
    return average

infile = open('USPopulation.txt', 'r')

population = infile.readlines()

infile.close()

print(f'Среднегодовое изменение численности населения в течение указанного периода времени: {calculate_average_annual_change(population)}')
print(f'Год с наибольшим увеличением численности населения в течение указанного периода времени: {max(population)}')
print(f'Год с наименьшим увеличением численности населения в течение указанного периода времени: {min(population)}')