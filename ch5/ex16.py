import random

def main():
    even = 0  #чётное
    odd = 0  #нечётное
    for count in range(1,101):
        number = random.randint(1,100)
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'Чётных - {even}\nНечётных - {odd}')

main()