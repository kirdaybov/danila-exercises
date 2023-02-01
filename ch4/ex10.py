semester = 145000
increase_percentage = 0.03

for year in range(1,6):
    cost_year = semester * 2
    cost_semester_increase = semester * increase_percentage
    semester += cost_semester_increase 
    print(f'Стоимость за {year} год обучения равно {cost_year:.1f}')