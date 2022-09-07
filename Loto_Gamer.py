import numpy as np
import random
from Loto_card import Loto_card


class Loto_Gamer:
    def __init__(self, name, ishuman):
        self.human = ishuman if type(ishuman) == bool else False   # человек или комп
        self.card = Loto_card() # карточка игрока
        self.name = name  # имя игрока

    def __str__(self):
        """
        Приведение объекта с строке
        """
        who = 'человек' if self.human else 'компьютер'
        return f'{self.name} ({who}): {str(self.card)}'

    def __eq__(self, other):
        # Сравнение по имени, человечности и карточкам
        result = isinstance(other, Loto_Gamer)
        if result:
            result = ((self.name == other.name) and (self.human == other.human) and (self.card == other.card))
        return result


    def can_move(self, keg_number):
        """
        можно делать ход - то есть есть ли выпавший номер в карточке
        :return: boolean - успех/неуспех
        """
        return (keg_number in self.card.getcard())

