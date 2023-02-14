import random

infile = open('8_ball_responses.txt', encoding = 'utf-8', mode = 'r')
answer = infile.readlines()
infile.close()

flag = 'Д'
random_index_for_answer = random.randint(0,len(answer) - 1)

print(answer)

flag = input('Если хотите задать вопрос нажмите "Д". Если хотите закрыть игру, любой другой символ.\n')

while flag.upper() == 'Д':
    user_question = input('Задайте свой вопрос:\n')
    print(answer[random_index_for_answer])
    flag = input('Если хотите задать вопрос ещё нажмите "Д". Если хотите закрыть игру, любой другой символ.\n')
print('Игра закрывается')

