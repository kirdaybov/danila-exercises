import random

num_comp = random.randint(1,3)

def Rock_Paper_Scissors_comp(num):
    if num == 1:
        print('камень')
        return('камень')
    elif num == 2:
        print('ножницы')
        return('ножницы')
    else:
        print('бумага')
        return("бумага")

def determine_who_wins(word1,word2):
    if word1 == "камень" or word2 == "камень" and word1 == "ножницы" or word2 == "ножницы":
        print("Побеждает камень")
    elif word1 == "ножницы" or word2 == "ножницы" and word1 == "бумага" or word2 == "бумага":
        print('Побеждают ножницы')
    elif word1 == "бумага" or word2 == "бумага" and word1 == "камень" or word2 == "камень":
        print('Побеждает бумага')
    else:
        print('Сыграйте ещё один раунд')

user_word = input('Введите "камень" или "ножницы" или "бумага"\n')
comp_word = Rock_Paper_Scissors_comp(num_comp)
print(f'Ваше слово - {user_word}. Слово компьютера - {comp_word}')
determine_who_wins(user_word, comp_word)