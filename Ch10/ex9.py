import random

class Question:
    def __init__(self, question, answer_1, answer_2, answer_3, answer_4, right_answer):
        self.__question = question
        self.__answer_1 = answer_1
        self.__answer_2 = answer_2
        self.__answer_3 = answer_3
        self.__answer_4 = answer_4
        self.__right_answer = right_answer

    def set_question(self, question):
        self.__question = question

    def set_answer_1(self, answer_1):
        self.__answer_1 = answer_1

    def set_answer_2(self, answer_2):
        self.__answer_2 = answer_2

    def set_answer_3(self, answer_3):
        self.__answer_3 = answer_3

    def set_answer_4(self, answer_4):
        self.__answer_4 = answer_4

    def set_right_answer(self, right_answer):
        self.__right_answer = right_answer

    def get_question(self):
        return self.__question

    def get_answer_1(self):
        return self.__answer_1

    def get_answer_2(self):
        return self.__answer_2

    def get_answer_3(self):
        return self.__answer_3

    def get_answer_4(self):
        return self.__answer_4

    def get_right_answer(self):
        return self.__right_answer

    def isCorrect(self, answer):
        return answer == self.get_right_answer()

    def __str__(self):
        result = self.get_question() + '\n' + \
                 '1. ' + self.get_answer_1() + '\n' + \
                 '2. ' + self.get_answer_2() + '\n' + \
                 '3. ' + self.get_answer_3() + '\n' + \
                 '4. ' + self.get_answer_4()
        return result

question_1 = Question('Выберите столицу России?','Париж','Москва','Берлин','Лисабон', 2)
question_2 = Question('Сколько лет Питеру?','320','403','298','342', 1)
question_3 = Question('Лучшая марка автомобиля?','Пежо','Рено','Порше','Ваз', 2)
question_4 = Question('Самое высокое дерево на земле?','Клён','Груша','Гиперион','Яблоня', 3)
question_5 = Question('Что весит больше? 1КГ ваты или 1КГ железа?','Железа','Ваты','Твоя задница','Весят одинаково', 4)
question_6 = Question('Самара расположилась вдоль реки...','Волга','Обь','Лена','Нева', 2)

dct_questions = []
dct_questions.append(question_1)
dct_questions.append(question_2)
dct_questions.append(question_3)
dct_questions.append(question_4)
dct_questions.append(question_5)
dct_questions.append(question_6)

index_random_question = random.randint(0,len(dct_questions) - 1)

player_1_points = 0
player_2_points = 0

for i in range(len(dct_questions)):
    if i % 2 == 0:
        player = 'Один'
    else:
        player = "Два"
    print(f'Вопрос для игрока {player} : ')
    current_question = dct_questions[index_random_question]
    print(current_question)
    user_answer = int(input('Введите ваше решение (номер между 1 и 4): '))
    if current_question.isCorrect(user_answer):
        if player == 'Один':
            player_1_points += 1
        else:
            player_2_points += 1
        print('Это правильный ответ!')
        print()
        del dct_questions[index_random_question]
    else:
        print(f'Ответ не правильный. Правильный ответ {current_question.get_right_answer()}')
        print()
        del dct_questions[index_random_question]

if player_1_points > player_2_points:
    print('Победил первый игрок')
elif player_2_points > player_1_points:
    print('Победил второй игрок')
else:
    print('Ничья!')
