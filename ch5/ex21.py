import random

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
    if word1 == word2:
        print(f"Ничья, оба выбрали {word1}")
    elif word1 == "камень":
        print("Побеждают ", "бумага" if word2 == "бумага" else "камень")
    elif word1 == "бумага":
        print("Побеждают ", "бумага" if word2 == "камень" else "ножницы")
    elif word1 == "ножницы":
        print("Побеждают ", "камень" if word2 == "камень" else "ножницы")

num_comp = random.randint(1,3)
user_word = input('Введите "камень" или "ножницы" или "бумага"\n')
comp_word = Rock_Paper_Scissors_comp(num_comp)
print(f'Ваше слово - {user_word}. Слово компьютера - {comp_word}')
determine_who_wins(user_word, comp_word)