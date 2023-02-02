def cost_class_A_seats(a):
    return a * 20

def cost_class_B_seats(b):
    return b * 20

def cost_class_C_seats(c):
    return c * 20

seats_A = int(input('Сколько было продано мест класса "А":\n'))    
seats_B = int(input('Сколько было продано мест класса "B":\n'))    
seats_C = int(input('Сколько было продано мест класса "C":\n'))  

cost_sets_A = cost_class_A_seats(seats_A)
cost_sets_B = cost_class_B_seats(seats_B)
cost_sets_C = cost_class_C_seats(seats_C)

def calculate_the_amount_of_income(num1, num2, num3):
    print(f'Сумма дохода - {num1 + num2 + num3} долларов')

calculate_the_amount_of_income(cost_sets_A, cost_sets_B, cost_sets_C)