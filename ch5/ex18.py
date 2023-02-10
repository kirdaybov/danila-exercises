import ex17

number = int(input('Введите число:\n'))

for x in range(1,101):
    if ex17.is_prime(x):
        print(x)
    