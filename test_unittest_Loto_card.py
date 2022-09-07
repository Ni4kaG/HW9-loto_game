import unittest
from Loto_card import Loto_card, NotOnCard

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card= Loto_card()
        self.thiscard = self.card.getcard()
    def tearDown(self):
        del self.card
        del self.thiscard

    def test_init(self):
        self.assertEqual(self.card.values_in_game, 15)
        self.assertEqual(len(self.thiscard), 3)
        self.assertEqual(sum(sum([x >= 0 for x in self.thiscard] )),27)
        self.assertEqual(sum(sum([x <= 90 for x in self.thiscard] )),27)

    def test_cross_out(self):
        a = 0
        torepeat = True
        for j in range(0,2):
            for i in range(0,9):
                a = self.thiscard[0,i]
                if a != 0:
                    torepeat = False
                    break
            if not torepeat:
                break
        self.card.cross_out(a)
        self.assertTrue(a in self.thiscard)
        self.assertEqual(self.card.values_in_game, 14)
        # проверка на ошибку
        with self.assertRaises(NotOnCard):
            self.card.cross_out(93)

    def test__eq__(self):
        c1 = Loto_card()
        c2 = Loto_card()
        c2.cross_out(c2.getcard()[1, 5])
        c3 = [1,2,3]
        self.assertTrue(c1 == c1)
        self.assertFalse(c1 == c3)
        self.assertFalse(c1 == c2)

    def test__str__(self):
        c1 = Loto_card()
        self.assertEqual(str(c1), f'Карточка лото 3х9, заполнены {c1.values_in_game} полей:\n{c1.getcard()}')
