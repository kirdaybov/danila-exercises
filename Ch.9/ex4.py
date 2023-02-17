inputfile = open('text.txt', 'r')
text = inputfile.readlines()
inputfile.close()

myset = set()

for word in text:
    word = word.rstrip()
    myset.add(word)

mylist = list(myset)

print(mylist)
