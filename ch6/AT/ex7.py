import os

found = False

search = input('Введите имя студента, которое нужно удалить:\n')

student_file = open('students.txt','r')

temp_file = open('temp.txt','w')

descr = student_file.readline()

while descr != '':
    descr = descr.rstrip('\n')
    if descr != search:
        temp_file.write(f'{descr}\n')
    else:
        found = True
    descr = student_file.readline

student_file.close()
temp_file.close()
os.remove('students.txt')
os.rename('temp.txt','students.txt')

if found:
    print('Файл обновлён')
else:
    print('Это значение не найдено')
