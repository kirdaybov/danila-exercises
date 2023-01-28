

pocket = int(input('Введите номер кармана - \n'))
if 0 <= pocket <= 36:
    if pocket == 0:
        print('Этот карман зелёный')
    elif 1 <= pocket <= 10 :
        if pocket % 2 == 0:
            print ('Этот карман чёрный')
        else:
            print ('Этот карман красный')
    elif 11 <= pocket <= 18:
        if pocket % 2 == 0:
            print ('Этот карман красный')
        else:
            print ('Этот карман чёрный')
    elif 19 <= pocket <= 28 :
        if pocket % 2 == 0:
            print ('Этот карман чёрный')
        else:
            print ('Этот карман красный')
    elif 29 <= pocket <= 36:
        if pocket % 2 == 0:
            print ('Этот карман красный')
        else:
            print ('Этот карман чёрный')
else:
    print('Вы ввели номер не из диапазона')