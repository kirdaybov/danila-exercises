number_file = open('numbers.txt','r')
file_contents = number_file.read()
number_file.close()

print(file_contents)