def is_prime(num):
    for x in range (2, num // 2 + 1): 
        if num % x == 0:
            return False             
    return True
        
user_number = int(input('Введите целое число больше 1:\n'))

list_numbers = []

for x in range(2,user_number + 1):
    if x <= user_number:
        list_numbers.append(x) 

for num in list_numbers:
    if is_prime(num):
        print(num, 'Это простое число') 
    else:
        print(num, 'Это не простое число') 

