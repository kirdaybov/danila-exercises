def is_prime(num):
    if num % num == 0 and num % 1 == 0 and num % 2 != 0:
        return True
    else:
        return False

for x in range(1,101):
    number = is_prime(x)
    if number == True:
        print(x)
    else:
        pass