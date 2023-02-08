numbers = [[4,9,2],[3,5,7],[8,1,6]]

def calculate_top_line(numbers):
    num1 = numbers[0][0]
    num2 = numbers[0][1]
    num3 = numbers[0][2]
    sum = num1 + num2 + num3
    return sum

def calculate_middle_line(numbers):
    num1 = numbers[1][0]
    num2 = numbers[1][1]
    num3 = numbers[1][2]
    sum = num1 + num2 + num3
    return sum
 
def calculate_bottom_line(numbers):
    num1 = numbers[2][0]
    num2 = numbers[2][1]
    num3 = numbers[2][2]
    sum = num1 + num2 + num3
    return sum
 
def diagonal1(numbers):
    num1 = numbers[0][0]
    num2 = numbers[1][1]
    num3 = numbers[2][2]
    sum = num1 + num2 + num3
    return sum

def diagonal2(numbers):
    num1 = numbers[0][2]
    num2 = numbers[1][1]
    num3 = numbers[2][0]
    sum = num1 + num2 + num3
    return sum

def LoShu(sum_top_line, sum_middle_line, sum_bottom_line, sum_diagonal1, sum_diagonal, column1, column2, column3):
    if sum_top_line == sum_middle_line == sum_bottom_line == sum_diagonal1 == sum_diagonal == column1 == column2 == column3:
        print('Этот список является магическим квадратом Ло Шу')
    else:
        print('Этот список не является магическим квадратом Ло Шу')

def column1(numbers):
    num1 = numbers[0][0]
    num2 = numbers[0][1]
    num3 = numbers[0][2]
    sum = num1 + num2 + num3
    return sum

def column2(numbers):
    num1 = numbers[1][0]
    num2 = numbers[1][1]
    num3 = numbers[1][2]
    sum = num1 + num2 + num3
    return sum

def column3(numbers):
    num1 = numbers[2][0]
    num2 = numbers[2][1]
    num3 = numbers[2][2]
    sum = num1 + num2 + num3
    return sum  
  
sum_top_line = calculate_top_line(numbers)
sum_middle_line = calculate_middle_line(numbers)
sum_bottom_line = calculate_bottom_line(numbers)
sum_diagonal1 = diagonal1(numbers)
sum_diagonal2 = diagonal2(numbers)
sum_column1 = column1(numbers)
sum_column2 = column2(numbers)
sum_column3 = column3(numbers)
total = LoShu(sum_top_line, sum_middle_line, sum_bottom_line, sum_diagonal1, sum_diagonal2, sum_column1, sum_column2, sum_column3)