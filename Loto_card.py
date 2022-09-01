import numpy as np
import random

class NotOnCard(Exception):

    def __str__(self):
        return 'Номера нет в карточке'

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
        else:
            raise NotOnCard()

    def getcard(self):
        return self.card            # почему-то просто обратиться к карточке не получилось без гета
