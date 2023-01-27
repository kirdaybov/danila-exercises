
def sum(number1, number2):
   sum = number1 + number2
   return sum

a = sum(1, 2)
#print(a)

def is_positive(num):
    if num > 0:
        print('positive')
    else: 
        print('not positive')

a = 0
#is_positive(a)

def sign(num):
    if num == 0:
        print('zero')
    else:    
        if num > 0:
            print('positive')
        else: 
            print('negatif')

#sign(0)
#sign(1)
#sign(-1)

def sign2(num):
    if num == 0:
        print('zero')
    elif num > 0:
        print('positive')
    else: 
        print('negatif')
       
def sum_sign(num1, num2):
    sign(sum(num1, num2))

d = -10

sum_sign(d, 9)