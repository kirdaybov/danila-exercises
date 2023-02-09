number = input('Введите набор чисел без разделителей:\n')
sum = 0
for num in number:
    if num.isdigit():
        num = int(num)
        sum += num
print("Сумма введёных Вами чисел -", sum)