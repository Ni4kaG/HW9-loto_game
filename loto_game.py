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


loto_kegs = [i for i in range(1, 91)]   #  номера бочонков от 1 до 90
random.shuffle(loto_kegs)               # перемешиваем

gamer1 = Loto_Gamer()
gamer1.name = input('Имя первого игрока: ')
answer = input('Ты чловек? y/n: ')
gamer1.human = (answer == 'y')

gamer2 = Loto_Gamer()
gamer2.name = input('Имя второго игрока: ')
answer = input('Ты чловек? y/n: ')
gamer2.human = (answer == 'y')

print(gamer1.name, '\n', gamer1.card.getcard())
print(gamer2.name, '\n', gamer2.card.getcard())


for loto_keg in loto_kegs:
    print(f'Выпал номер ', loto_keg)
    if gamer1.human:
        answer = input(gamer1.name+', ты будешь ходить? (y/n): ')
        if (answer == 'y') == gamer1.can_move(loto_keg):
            gamer1.card.cross_out(loto_keg)
        else:
            print(gamer1.name,' проиграл! Игра окончена досрочно!')
            break
    else:
        gamer1.card.cross_out(loto_keg)

    if gamer2.human:
        answer = input(gamer2.name + ', ты будешь ходить? (y/n): ')
        if (answer == 'y') == gamer2.can_move(loto_keg):
            gamer2.card.cross_out(loto_keg)
        else:
            print(gamer2.name,' проиграл! Игра окончена досрочно!')
            break
    else:
        gamer2.card.cross_out(loto_keg)


    if gamer1.card.values_in_game == 0 and gamer2.card.values_in_game == 0:
        print('Игра окончена. Ничья!!!')
        break
    elif gamer1.card.values_in_game == 0:
        print(gamer1.name,' выграл со счетом ', 15-gamer1.card.values_in_game, ':', 15-gamer2.card.values_in_game)
        break
    elif gamer2.card.values_in_game == 0:
        print(gamer2.name,' выграл со счетом ', 15-gamer2.card.values_in_game, ':', 15-gamer1.card.values_in_game)
        break
    else:
        print(gamer1.name, '\n', gamer1.card.getcard())
        print(gamer2.name, '\n', gamer2.card.getcard())