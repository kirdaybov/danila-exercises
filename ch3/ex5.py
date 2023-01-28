mas = float(input('Введите масу тела в кг: \n'))
weight = mas * 9.8
if weight > 500:
    print("тело слишком тяжелое")
elif weight < 100:
    print("тело слишком лёгкое")
else:
    print("Вес равен = ", weight)