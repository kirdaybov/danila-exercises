def is_prime(num):
    for x in range (2, num // 2): 
        if num % x == 0:
            print('F')
            return False
    print('T')
    return True
number = int(input('Введите число:\n'))

is_prime(number)


