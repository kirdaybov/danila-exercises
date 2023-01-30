vegetarian = input('Будет ли на ужине вегетарианец? Напишите "Y" если да, "N" - если нет\n')
vegan = input('Будет ли на ужине веганец? Напишите "Y" если да, "N" - если нет\n')
gluten = input('Будет ли на ужине приверженец безглютеновой диеты? Напишите "Y" если да, "N" - если нет\n')
if vegetarian.upper() == 'Y' and vegan.upper() == 'Y' and gluten.upper() == 'Y':
    print('Вот Ваши варианты ресторанов:\nКафе за углом\nКухня шеф-повара')
elif vegetarian.upper() == 'Y' and vegan.upper() == 'Y' and gluten.upper() == 'N':
    print('Вот Ваши варианты ресторанов:\nКафе за углом\nКухня шеф-повара')
elif vegetarian.upper() == 'Y' and vegan.upper() == 'N' and gluten.upper() == 'N':
    print('Вот Ваши варианты ресторанов:\nКафе за углом\nКухня шеф-повара\nЦентральная пиццерия\nБлюда от итальянской мамы')
elif vegetarian.upper() == 'N' and vegan.upper() == 'N' and gluten.upper() == 'N':
    print('Вот Ваши варианты ресторанов:\nКафе за углом\nКухня шеф-повара\nЦентральная пиццерия\nБлюда от итальянской мамы\nИзысканные гамбургеры от Джо')
elif vegetarian.upper() == 'N' and vegan.upper() == 'Y' and gluten.upper() == 'N':
    print('Вот Ваши варианты ресторанов:\nКафе за углом\nКухня шеф-повара')
elif vegetarian.upper() == 'N' and vegan.upper() == 'N' and gluten.upper() == 'Y':
    print('Вот Ваши варианты ресторанов:\nКафе за углом\nКухня шеф-повара\nЦентральная пиццерия')
elif vegetarian.upper() == 'N' and vegan.upper() == 'Y' and gluten.upper() == 'Y':
    print('Вот Ваши варианты ресторанов:\nКафе за углом\nКухня шеф-повара')
elif vegetarian.upper() == 'Y' and vegan.upper() == 'N' and gluten.upper() == 'Y':
    print('Вот Ваши варианты ресторанов:\nКафе за углом\nКухня шеф-повара\nЦентральная пиццерия')   
else:
    print('Вы нажали не тот символ')