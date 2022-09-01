import numpy as np
import random



class Loto_card:
    def __init__(self):
        self.card = np.zeros((3, 9), int)
        for x in range(0, 3):               # будем заполнять карточку построчно (3 строки по 9 чисел)
            a = [i for i in range(1, 10)]   # массив с индексами от 1 до 9
            random.shuffle(a)               # перемешиваем его случайным образом
            b = [a[i] for i in range(0, 5)] # первые пять индексов будут содержать в х-той строке номера
            for i in range(0, 9):           # в первом столбце числа от 1 до 10, во втором от 11 до 20 и т.д.
                arr_temp = [k for k in range(1 + i * 10, 10 * (i + 1)) if k not in self.card]  # чтобы не повторялись номера, исключим то, что уже есть в карточке
                self.card[x, i] = random.choice(arr_temp) if (i + 1) in b else 0  # случайное число из нужного диапазона, и на место с выбранным индексом для ненулевого значения
        self.values_in_game = 15   # в игре будет по 5 номеров в каждой из трех строк = 15 номеров, по мере игры будем уменьшать при вычеркивании

    def cross_out(self, what):     # вычеркнуть из карточки номер what
        if what in self.card:
           self.card = np.where(self.card != what, self.card, 0)        # обнуляем если есть выпавший номер
           self.values_in_game -= 1 if self.values_in_game > 0 else 0  # уменьшаем число значений в игре

    def getcard(self):
        return self.card            # почему-то просто обратиться к карточке не получилось без гета




class Loto_Gamer:
    def __init__(self):
        self.human = True  # человек или комп
        self.card = Loto_card() # карточка игрока
        self.name = ''  # имя игрока

    def can_move(self, what):
        """
        можно делать ход - то есть есть ли выпавший номер в карточке
        :return: boolean - успех/неуспех
        """
        return (what in self.card.getcard())


# определим игроков:
gamer_num = int(input('Задайте количество игроков: '))
gamer_list = []

for n in range(0,gamer_num):
    gamer = Loto_Gamer()
    gamer.name = input(f'Имя {n+1}-го игрока: ')
    answer = input('Ты чловек? y/n: ')
    gamer.human = (answer == 'y')
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
