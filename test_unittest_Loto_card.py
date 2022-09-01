import unittest
from Loto_card import Loto_card

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card= Loto_card()
        self.thiscard = self.card.getcard()
    def tearDown(self):
        del self.card

    def test_init(self):
        self.assertEqual(self.card.values_in_game, 15)
        self.assertEqual(len(self.thiscard), 3)
#        self.assertEqual(all(map(lambda p: isinstance(p, int), self.thiscard[0])), True)
        self.assertEqual(sum(sum([x >= 0 for x in self.thiscard] )),27)
        self.assertEqual(sum(sum([x <= 90 for x in self.thiscard] )),27)

    def test_cross_out(self):
        for i in range(0,9):
            a = self.thiscard[0,i]
            if a != 0:
                break
        self.assertEqual(self.card.cross_out(self.thiscard,a), True)
        self.assertEqual(self.card.cross_out(self.thiscard, 92), False)
        pass
