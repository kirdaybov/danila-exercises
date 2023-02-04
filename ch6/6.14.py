any_file = open('data.txt', 'r')
line = any_file.readline()
while line != '':
    print(line)
    line = any_file.readline()
any_file.close()