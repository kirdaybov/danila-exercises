
def calculate_error(right_answers, answers):
    errors = []
    for index in range(len(right_answers)):
        if right_answers[index] != answers[index]:
            errors.append(index) 
    return errors

def read_answers(file_name):
    infile = open(file_name, 'r')
    user_answers = infile.readlines()
    infile.close()
    index = 0
    while index < len(user_answers):
        user_answers[index] = user_answers[index].rstrip('\n')
        index += 1
    return user_answers

def is_passed(errors):
    if len(errors) > 5:
        print('Вы лох и не прошли. Хе-хе)')
    else:
        print('Вы красавчик!')

def right_answer_count(errors, right_answers):
    count_error = len(right_answers) - len(errors)
    right_answer = len(right_answers) - count_error
    print(f'Кол-во ошибок: {count_error}')
    print(f'Кол-во правильных ответов: {right_answer}')

right_answers = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']
user_answers = read_answers()
errors = calculate_error(right_answers,user_answers)
is_passed(errors)
right_answer_count(errors,right_answers)
print(f'Неправильные ответы: {errors}')        


#Прочитать ещё раз про APPEND