test_answers = ['A','C','A','A','D','B','C','A','C','B','A','D','C','A','D','C','B','B','D','A']

infile = open('student_solution.txt', 'r')

user_answers = infile.readlines()

infile.close()

index = 0
while index < len(user_answers):
    user_answers[index] = user_answers[index].rstrip('\n')
    index += 1



def calculate_error(list1,list2):
    error = 0
    for index in range(len(list1)):
        answer1 = list1[index]
        
    for index in range(len(list2)):
        answer2 = list2[index]
        

    if answer1 == answer2:
        error += 1

    print('Кол-во ошибок:',error)

calculate_error(test_answers,user_answers)
        

        




