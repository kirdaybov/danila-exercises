infile = open('text.txt', 'r')

file = infile.readlines()

infile.close()

number_words = 0
number_of_sentences = 0

for line in file:
    number_of_sentences += 1
    number_words += len(line.split())
    
print(f'Всего предложений - {number_of_sentences}\nВсего слов - {number_words}\nСреднее кол-во слов на предложение - {number_words / number_of_sentences:.1f}')


