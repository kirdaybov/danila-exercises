def calculate_vowels(line):
    vowels = 0
    for sumbol in line:
        if sumbol == 'а' or sumbol == 'у' or sumbol == 'е' or sumbol == 'ы' or sumbol == 'а' or sumbol == 'о' or sumbol == 'э' or sumbol == 'и' or sumbol == 'ю':
            vowels += 1
    return vowels

#def calculate_consonants(line):

line = 'а а а у'

print('Всего гласных в строке - ',calculate_vowels(line))
