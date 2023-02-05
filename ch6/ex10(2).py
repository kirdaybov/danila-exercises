player_file = open('golf.txt', 'r')

name_player = player_file.readline()

while name_player != '':
    player_points = int(player_file.readline())
    name_player = name_player.rstrip('\n')
    print(f'Игрок: {name_player}')
    print(f'Очки: {player_points}')
    name_player = player_file.readline()

player_file.close()