inputfile = open('Kennedy.txt',encoding = 'utf-8', mode = 'r')
text = inputfile.read()
inputfile.close()

words = text.split()
lines = text.split('\n')

dict_words = {}
for word in words:
    dict_words[word] = []
    for index in range(len(lines)):
        line = lines[index]
        line = line.split()
        if word in line:
            dict_words[word].append(index + 1)

outfile = open('index_word.txt', 'w')
for key,value in dict_words.items():
    print(f'{key}: ', end='', file=outfile)
    for num in value:
        print(f'{num} ', end='',file=outfile)
    print(file=outfile)
outfile.close()

