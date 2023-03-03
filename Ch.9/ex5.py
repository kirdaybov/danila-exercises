inputfile = open('text.txt', 'r')
text = inputfile.read()
inputfile.close()

dict_words = {}

words = text.split()

for word in words:
    word = word.rstrip()
    if word not in dict_words:
        dict_words[word] = 1
    elif word in dict_words:
        dict_words[word] += 1

print(dict_words)

