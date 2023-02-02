def calculate_fats(gramm_of_fat):
    print(f'калории за жиры - {gramm_of_fat * 9}')

def calculate_carbohydrates(gramm_of_carbohydrates):
    print(f'калории за углеводы - {gramm_of_carbohydrates * 4}')

fat = float(input('Введите кол-во граммов жиров:\n'))
carbohydrates = float(input('Введите кол-во граммов углеводов:\n'))
calculate_fats(fat)
calculate_carbohydrates(carbohydrates)

