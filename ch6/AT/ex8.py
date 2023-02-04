import os

found = False

search = input('Введите имя студента, оценку которого нужно изменить:\n')
new_qty = int(input('Введите новую оценку:\n'))

student_file = open('students.txt','r')

temp_file = open('temp.txt','w')

descr = student_file.readline()

while descr != '':
    qty = int(student_file.readline())
    descr = descr.rstrip('\n')
    if descr == search:
        temp_file.write(f'{descr}\n')
        temp_file.write(f'{new_qty}\n')
        found = True
    else:
        temp_file.write(f'{descr}\n')
        temp_file.write(f'{qty}\n')
    descr = student_file.readline

student_file.close()
temp_file.close()
os.remove('students.txt')
os.rename('temp.txt','students.txt')

if found:
    print('Файл обновлён')
else:
    print('Это значение не найдено')

