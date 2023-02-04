#name_file = input('Введите название файла:\n')

#total = 5

file_5str = open('my_name..txt','r')
for line in file_5str(1,6):
    print(line)

file_5str.close()