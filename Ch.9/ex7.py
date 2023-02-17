def count_of_wins(words):
    dict_teams = {}
    for word in words:
        if word not in dict_teams:
            dict_teams[word] = 1
        elif word in dict_teams:
            dict_teams[word] += 1
    return dict_teams

def years_wins(words):
    dict_years = {}
    year = 1902
    for word in words:
        year += 1
        dict_years[year] = word
    return dict_years
        
inputfile = open('WorldSeriesWinners.txt',encoding = 'utf-8', mode = 'r')
text = inputfile.read()
inputfile.close()

words = text.split('\n')

user_year = int(input('Введите год в диапазоне от 1903 до 2009:\n'))

if user_year == 1904 or user_year == 1994:
    print('В этом году Мировая серия не проводилась')
elif 2009 >= user_year >= 1903:    
    who_has_won = years_wins(words)
    team = who_has_won[user_year]
    dict_team = count_of_wins(words)
    count_wins_user_team = dict_team[team]
    print(f'В этом году победила:{team}\nВ период с 1903 по 2009 {team} побеждала {count_wins_user_team}')
else:
    print('Вы ввели недопустимое значение')



