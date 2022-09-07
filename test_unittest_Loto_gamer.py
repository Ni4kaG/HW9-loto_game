import unittest
from Loto_Gamer import Loto_Gamer, Loto_card

class TestGamer(unittest.TestCase):

    def setUp(self):
        self.gamer= Loto_Gamer('Nika', 'да')

    def tearDown(self):
        del self.gamer

    def test_init(self):
        self.assertEqual(self.gamer.name, 'Nika')
        self.assertFalse(self.gamer.human)
        self.assertEqual(self.gamer.card.values_in_game,15)


    def test_can_move(self):
        a = 0
        to_repeat = True
        for j in range(0,2):
            for i in range(0,9):
                a = self.gamer.card.getcard()[j,i]
                if a != 0:
                    to_repeat = False
                    break
            if not to_repeat:
                break

        self.assertTrue(self.gamer.can_move(a))
        self.assertFalse(self.gamer.can_move(92))

    def test_gamer(self):
        self.gamer.name = 'Nika'
        self.gamer.human = True
        self.assertEqual(self.gamer.name, 'Nika')
        self.assertTrue(self.gamer.human)

    def test__eq__(self):
        g1 = Loto_Gamer('Nika', True)
        g2 = Loto_Gamer('Gena', False)
        g3 = [1, 2, 3]
        g4 = Loto_Gamer('Gena', True)
        g4.card = g2.card

        g5 = Loto_Gamer('Nika', False)
        g5.card = g2.card

        self.assertTrue(g1 == g1)
        self.assertFalse(g1 == g3)
        self.assertFalse(g2 == g4)
        self.assertFalse(g2 == g5)
        self.assertFalse(g4 == g5)

    def test__str__(self):
        g1 = Loto_Gamer('Nika', True)
        self.assertEqual(str(g1),f'Nika (человек): {str(g1.card)}')