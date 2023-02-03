grade1 = int(input('Введите первую оценку:\n'))
grade2 = int(input('Введите вторую оценку:\n'))
grade3 = int(input('Введите третью оценку:\n'))
grade4 = int(input('Введите четвёртую оценку:\n'))
grade5 = int(input('Введите пятую оценку:\n'))

def calc_average(num1, num2, num3, num4, num5):
    number_of_ratings = 5
    sum_grade = num1 + num2 + num3 + num4 + num5
    average = sum_grade // number_of_ratings
    print(f'Средний балл - {average}')
    return average

def determine_grade(average):
    if average >= 90:
        print('Оценка "А"') 
    elif 80 <= average <= 89:
        print('Оценка "B"') 
    elif 70 <= average <= 79:
        print('Оценка "C"') 
    elif 60 <= average <= 69:
        print('Оценка "D"') 
    else:
        print('Оценка "F"')

average = calc_average(grade1, grade2, grade3, grade4, grade5)
determine_grade(average)