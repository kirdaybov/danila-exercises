def set_creation(text):
    myset = set()
    words = text.split()
    for word in words:
        word = word.rstrip()
        myset.add(word)
    return myset

#Читаем первый текстовый файл
inputfile = open('text.txt',encoding = 'utf-8', mode = 'r')
text_1 = inputfile.read()
inputfile.close()

#Читаем второй текстовый файл
inputfile = open('text_2.txt', encoding = 'utf-8', mode = 'r')
text_2 = inputfile.read()
inputfile.close()

set_text_1 = set_creation(text_1)
set_text_2 = set_creation(text_2)

print(f'Список слов, входящих в оба файла: {set_text_1 & set_text_2}')
print(f'Список слов входящий либо в первый, либо во второй, но не входящий в обо файла одновременно: {set_text_1.symmetric_difference(set_text_2)}')
print(f'Список слов из первого файла, не входящий во второй: {set_text_1 - set_text_2}')
print(f'Список слов из второго файла, не входящий в первый: {set_text_2 - set_text_1}')
print(f'Список всех слов: {set_text_1 | set_text_2}')