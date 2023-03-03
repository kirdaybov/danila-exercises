import random

def ace(player):
    if player <= 9:
        ace = 11
        player = player + ace
    elif player > 9:
        ace = 1
        player = player + ace
    return player

deck = {'Туз пик':1,'2 пик':2,'3 пик':3, '4 пик':4,'5 пик':5,'6 пик':6, '7 пик':7,'8 пик':8,'9 пик':9,'10 пик':10,'Валет пик':10, 'Дама пик':10,'Король пик':10,
'Туз червей':1,'2 червей':2,'3 червей':3, '4 червей':4,'5 червей':5,'6 червей':6, '7 червей':7,'8 червей':8,'9 червей':9,'10 червей':10,'Валет червей':10, 'Дама червей':10,'Король червей':10,
'Туз треф':1,'2 треф':2,'3 треф':3, '4 треф':4,'5 треф':5,'6 треф':6, '7 треф':7,'8 треф':8,'9 треф':9,'10 треф':10,'Валет треф':10, 'Дама треф':10,'Король треф':10,
'Туз бубей':1,'2 бубей':2,'3 бубей':3, '4 бубей':4,'5 бубей':5,'6 бубей':6, '7 бубей':7,'8 бубей':8,'9 бубей':9,'10 бубей':10,'Валет бубей':10, 'Дама бубей':10,'Король бубей':10,
}

player_1 = 0
player_2 = 0

for card in deck:
    card_1 = random.choice(list(deck))
    card_2 = random.choice(list(deck))
    if player_1 < 21 and player_2 < 21:
        if card_1 == 'Туз пик' or card_1 == 'Туз червей' or card_1 == 'Туз треф' or card_1 == 'Туз бубей':
            player_1 = ace(player_1)
        else:        
            player_1 = player_1 + deck[card_1]
        print(f"Первый игрок получил карту {card_1}. Сумма карт на его руке {player_1}")
        if card_2 == 'Туз пик' or card_2 == 'Туз червей' or card_2 == 'Туз треф' or card_2 == 'Туз бубей':
            player_2 = ace(player_2)
        else:
            player_2 = player_2 + deck[card_2]
        print(f"Второй игрок получил карту {card_2}. Сумма карт на его руке {player_2}")
    elif player_1 > 21 and player_2 > 21:
        print('Проиграли оба')
        break
    elif player_1 > player_2:
        print('Победил второй игрок') 
        break
    else:
        print('Победил первый игрок') 
        break




