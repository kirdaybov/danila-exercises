Audience = {'CS101': "3004", 'CS102': "4501", 'CS103': "6755", 'NT110': '1244', 'CM241': '1411'}
teacher = {'CS101': "Хайнс", 'CS102': "Альварадо", 'CS103': "Рич", 'NT110': 'Берк', 'CM241': 'Ли'}
time = {'CS101': "8:00", 'CS102': "9:00", 'CS103': "10:00", 'NT110': '11:00', 'CM241': '13:00'}

course_number = input('Введите номер курса:\n')

if course_number in Audience:
    print(f'Вам нужно в аудиторию {Audience[course_number]}')
    print(f'Ваш преподаватель - {teacher[course_number]} ')
    print(f'Ваша пара начинается в {time[course_number]}')
else:
    print('Вы ввели не существующий курс или курс за которым не закрепленна аудитория')
