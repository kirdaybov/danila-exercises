outfile = open('number_list.txt', 'w')

for count in range(1,101):
    number = count
    outfile.write(f'{count}\n')

outfile.close()
print ('Данные записаны в number_list.txt')

