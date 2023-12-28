import unittest
from juego import valor_mano

class TestValorMano(unittest.TestCase):

    def test_sin_ases(self):
        mano = [('5', 'Corazones'), ('K', 'Picas')]
        self.assertEqual(valor_mano(mano), 15)

    def test_con_un_as(self):
        mano = [('A', 'Diamantes'), ('9', 'Corazones')]
        self.assertEqual(valor_mano(mano), 20)

    def test_con_multiples_ases(self):
        mano = [('A', 'Tréboles'), ('A', 'Diamantes'), ('9', 'Picas')]
        self.assertEqual(valor_mano(mano), 21)

    def test_excediendo_21_con_ases(self):
        mano = [('A', 'Tréboles'), ('9', 'Picas'), ('A', 'Diamantes'), ('3', 'Corazones')]
        self.assertEqual(valor_mano(mano), 14)
