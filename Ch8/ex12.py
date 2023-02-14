sentence = input('Введите своё предложение:\n')

sentence = sentence.upper()

youth_sentence = []

for word in sentence.split():
    youth_word = word[1:] + word[0] + 'КИ'
    youth_sentence.append(youth_word) 

print(' '.join(youth_sentence))



