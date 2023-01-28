color1 = str(input('Цвет 1: Введите или "красный" или "синий" или "желтый": \n'))
color2 = str(input('Цвет 2: Введите или "красный" или "синий" или "желтый": \n'))
if color1!='красный' and color1!='синий' and color1!='желтый' :
    print('Вы неправильно написали первый цвет')
elif color2!='красный' and color2!='синий' and color2!='желтый':
    print('Вы неправильно написали второй цвет')
elif color1 =='красный' or color2 =='красный' and color1 =='синий' or color2 =='синий':
    print('получится фиолетовый')
elif color1 =='красный' or color2 =='красный' and color1 =='желтый' or color2 =='желтый':
    print('получится оранжевый')
elif color1 =='синий' or color2 =='синий' and color1 =='желтый' or color2 =='желтый':
    print('получится зелёный')