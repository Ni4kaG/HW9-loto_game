import numpy as np
import random
from Loto_card import Loto_card


class Loto_Gamer:
    def __init__(self, name, ishuman):
        self.human = ishuman if type(ishuman) == bool else False   # человек или комп
        self.card = Loto_card() # карточка игрока
        self.name = name  # имя игрока

    def can_move(self, keg_number):
        """
        можно делать ход - то есть есть ли выпавший номер в карточке
        :return: boolean - успех/неуспех
        """
        return (keg_number in self.card.getcard())
