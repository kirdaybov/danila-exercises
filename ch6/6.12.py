number_file = open('number.txt', "w")

for x in range(1,11):
    number = x
    number_file.write(str(x) + '\n')

number_file.close()
