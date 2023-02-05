another = 'Y'

player_file = open('golf.txt', 'w')

while another.upper() == 'Y':
    name_player = input('Введите имя игрока:\n')
    player_points = int(input('Введите его счёт:\n'))
    player_file.write(f'{name_player}\n')
    player_file.write(f'{player_points}\n')
    another = input('Желаете добавить ещё игроков? Если да, введите "Y":\n')

player_file.close()
print ('Данные добавлены в "golf.txt"')




