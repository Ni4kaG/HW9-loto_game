import numpy as np
import random
from Loto_card import Loto_card
from Loto_Gamer import Loto_Gamer

# определим игроков:
gamer_num = int(input('Задайте количество игроков: '))
gamer_list = []

for n in range(0,gamer_num):

    name = input(f'Имя {n+1}-го игрока: ')
    human = (input('Ты чловек? y/n: ') == 'y')
    gamer = Loto_Gamer(name, human)
    gamer_list.append(gamer)
    print(gamer.name, '\n', gamer.card.getcard())

# играем:
loto_kegs = [i for i in range(1, 91)]   #  номера бочонков от 1 до 90
random.shuffle(loto_kegs)               # перемешиваем
game_over = False
move_num = 0
for loto_keg in loto_kegs:
    move_num +=1
    print(f'Выпал номер ', loto_keg)
    for gamer in gamer_list:
        if gamer.human:
            answer = input(gamer.name+', ты будешь ходить? (y/n): ')
            if (answer == 'y') == gamer.can_move(loto_keg):
                gamer.card.cross_out(loto_keg)
            else:
                print(f'{gamer.name} проиграл! Игра окончена досрочно на {move_num}-м ходу!')
                game_over = True
                break
        else:
            gamer.card.cross_out(loto_keg)
        if gamer.card.values_in_game == 0:
            print(f'{gamer.name} выграл! Игра окончена на {move_num}-м ходу!')
            game_over = True
            break

        else:
            print(gamer.name, '\n', gamer.card.getcard())
    if game_over:
        break
