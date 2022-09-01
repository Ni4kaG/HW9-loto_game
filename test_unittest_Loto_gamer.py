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
