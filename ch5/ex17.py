def is_prime(num):
    if num % num == 0 and num % 1 == 0 and num % 2 != 0:
        print('T')
        return True
    else:
        print('F')
        return False

number = int(input('Введите число:\n'))

is_prime(number)
