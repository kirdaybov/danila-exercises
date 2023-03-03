import random

countries = {'Россия' : 'Москва', 'Германия' : 'Берлин', 'Франция' : 'Париж', 'Португалия' : 'Лисабон'}

user_error = 0
user_right_answer = 0
answer = 0
flag = 'Д'

try:
    while flag == 'Д':
        keys = list(countries.keys())
        random_key = keys[random.randint(0,len(keys)- 1)]
        right_answer = countries[random_key]
        print(f'Введите столицу страны {random_key}')
        answer_user = input('')
        if answer_user == right_answer:
            user_right_answer += 1
        else:
            user_error += 1
        answer += 1
        print(f'Всего ответов: {answer}\nПравильных ответов: {user_right_answer}\nОшибок: {user_error}')
        flag = input('Если хотите ещё поиграть, нажмите "Д"\n')
        flag = flag.upper()
        countries.pop(random_key)
        if not countries:
            print("К сожалению, кончились вопросы")
            break   
    print(f'Всего ответов: {answer}\nПравильных ответов: {user_right_answer}\nОшибок: {user_error}\nВсего доброго!')
except:
    print(f'К сожалению, что-то пошло не так')

