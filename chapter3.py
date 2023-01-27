#number = int(input("Введите число в диапазоне от 1 до 7: \n"))
#if number == 1 :
    #print("Понедельник")
#elif number == 2:
    #print("Вторник")
#elif number == 3:
    #print("Среда")    
#elif number == 4:
    #print("Четверг")
#elif number == 5:
    #print("Пятница")
#elif number == 6:
    #print("Суббота")
#elif number == 7:
    #print("Воскресенье")
#else:
#    print("Ошибка, вы ввели не то")

#rectangle_width1 = int(input("Введите ширину прямоугольника 1: \n"))
#rectangle_lengths1 = int(input("Введите длину прямоугольника 1: \n"))
#rectangle_width2 = int(input("Введите ширину прямоугольника 2: \n"))
#rectangle_lengths2 = int(input("Введите длину прямоугольника 2: \n"))
#area_of_a_rectangle1 = rectangle_width1 * rectangle_lengths1
#area_of_a_rectangle2 = rectangle_width2 * rectangle_lengths2
#if area_of_a_rectangle1 > area_of_a_rectangle2:
    #print("Площадь первого прямоугольника больше")
#elif area_of_a_rectangle1 < area_of_a_rectangle1:
    #print ("Площадь второго прямоугольника больше")
#elif area_of_a_rectangle1 == area_of_a_rectangle2:
    #print("Площадь прямоугольников равна")

#age = int(input("Введите возраст: \n"))
#if age <= 1:
    #print("младенец")
#elif 1 < age < 13:
    #print("ребёнок")
#elif 13 <= age < 20:
    #print("подросток")
#elif 20 <= age:
    #print("взрослый")

#d = {1: 'I', 2: 'II', 3: 'III' ,4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X'}
#number = int(input('Введите число от 1 до 10 \n'))
#if 1<= number <= 10:
    #print(f'{number}: {d[number]}')
#else:
    #print('Вы ввели число не из диапазона')

#mas = float(input('Введите масу тела в кг: \n'))
#weight = mas * 9.8
#if weight > 500:
    #print("тело слишком тяжелое")
#elif weight < 100:
    #print("тело слишком лёгкое")
#else:
    #print("Вес равен = ", weight)


#month = int(input('Введите месяц в числовой форме: \n'))
#day = int(input('Введите день в числовой форме: \n'))
#year = int(input('Введите двузначный год в числовой форме: \n'))
#magic_date = month * day
#if magic_date == year:
    #print('Данная дата магическая')
#else:
    #print('Данная дата не магическая')

color1 = str(input('Цвет 1: Введите или "красный" или "синий" или "желтый": \n'))
color2 = str(input('Цвет 2: Введите или "красный" или "синий" или "желтый": \n'))
if color1!='красный' and color1!='синий' and color1!='желтый' :
    print('Вы неправильно написали первый цвет')
elif color2!='красный' and color2!='синий' and color2!='желтый':
    print('Вы неправильно написали второй цвет')
elif color1 and color2 == 'красный' and color1 and color2 == 'синий':
    print('получится фиолетовый')
elif color1 and color2 == 'красный' and color1 and color2 == 'желтый':
    print('получится оранжевый')
elif color1 and color2 == 'синий' and color1 and color2 == 'желтый':
    print('получится зелёный')

#people = int(input('Сколько участников пикника? \n'))
#hot_dog = int(input('Сколько хот-догов одному человеку? \n'))
#package_sosige = 10
#package_broud = 8
#total_hot_dog = people * hot_dog
#total_hot_dog_broud = total_hot_dog * 2
#print ('Всего нужно сосисок - ', total_hot_dog)
#print('Всего нужно булок - ', total_hot_dog_broud)
#total_sosige_package = total_hot_dog / package_sosige
#total_broud_package =  total_hot_dog_broud / package_broud
#print('всего пачек сосисок понадобится - ', total_sosige_package)
#print('всего пачек булок понадобится - ', total_broud_package)
# не совсем понятно, как сделать так чтобы програма считала задействованые пакеты и остаток в них

