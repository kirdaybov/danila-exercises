def mounth(dates):
    if dates[1] == '01':
        month_text = ('Января')
        return month_text
    elif dates[1] == '02':
        month_text = ('Февраля')
        return month_text
    elif dates[1] == '03':
        month_text = ('Марта')
        return month_text
    elif dates[1] == '04':
        month_text = ('Апреля')
        return month_text
    elif dates[1] == '05':
        month_text = ('Мая')
        return month_text
    elif dates[1] == '06':
        month_text = ('Июня')
        return month_text
    elif dates[1] == '07':
        month_text = ('Июля')
        return month_text
    elif dates[1] == '08':
        month_text = ('Августа')
        return month_text
    elif dates[1] == '09':
        month_text = ('Сентября')
        return month_text
    elif dates[1] == '10':
        month_text = ('Октября')
        return month_text
    elif dates[1] == '11':
        month_text = ('Ноября')
        return month_text
    elif dates[1] == '12':
        month_text = ('Декабря')
        return month_text
    else:
        print('Ввели недопустимое значение для месяца')
        quit()

dates = input('Введите дату в формате "дд/мм/гггг:\n')

dates = dates.split('/')

month_text = mounth(dates)
print(f'{dates[0]} {month_text} {dates[2]}')