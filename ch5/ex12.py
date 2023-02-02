def max(num1,num2):
    if num1 > num2:
        print(num1, "больше")
        return num1
    elif num2 > num1:
        print(num2, "больше")
        return num2
    else:
        print('Вы ввели одинаковые числа')
    
num1 = int(input('Введите первое число:\n'))
num2 = int(input('Введите второе число:\n'))

max(num1,num2)