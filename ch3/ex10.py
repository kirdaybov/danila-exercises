kopeyka5 = 5
kopeyka10 = 10
kopeyka50 = 50
victory = 100

useranswer_kopeyka5 = int (input('Напишите число, сколько 5-ти значных копеек взять - \n'))
useranswer_kopeyka10 = int (input('Напишите число, сколько 10-ти значных копеек взять - \n'))
useranswer_kopeyka50 = int (input('Напишите число, сколько 50-ти значных копеек взять - \n'))

total_kopeyka5 = kopeyka5 * useranswer_kopeyka5
total_kopeyka10 = kopeyka10 * useranswer_kopeyka10
total_kopeyka50 = kopeyka50 * useranswer_kopeyka50

total_sum = total_kopeyka5 + total_kopeyka10 + total_kopeyka50
print('Ваша сумма равна - ', total_sum, 'копейкам')
if total_sum < victory:
    print('Ваша сумма меньше 1-го рубля')
elif total_sum > victory:
    print('Вышв сумма больше рубля')
else:
    print('Вы красавчик!')