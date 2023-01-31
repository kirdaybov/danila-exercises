second = int(input('Введите кол-во секунд - \n '))
if  60 <= second < 3600:
    minute = second // 60
    second = second % 60
    print('Число минут равно - ', minute, '\nЧисло секунд равно - ', second)
elif 3600 <= second <= 86400:
    hour = second // 3600
    second = second - (hour * 3600)
    minute = second // 60
    second = second - (minute * 60)
    print('Число часов равно - ', hour,'Число минут равно - ', minute, '\nЧисло секунд равно - ', second)
elif second > 86400:
    day = second // (24 * 3600)
    second = second - (day * 24 * 3600)
    hour = second // 3600
    second = second - (hour * 3600)
    minute = second // 60
    second = second - (minute * 60)
    print('Число дней равно - ', day,'Число часов равно - ', hour,'Число минут равно - ', minute, '\nЧисло секунд равно - ', second)
else:
    print('Число секунд - ', second) 