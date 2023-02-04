import ex17

number = int(input('Введите число:\n'))

for x in range(1,101):
    number = ex17.is_prime(x)
    if number == True:
        print(x)
    