import unittest
from juego import valor_mano

class TestValorMano(unittest.TestCase):
    def test_sin_ases(self):
        self.assertEqual(valor_mano([('5', ''), ('7', '')]), 12)
        self.assertEqual(valor_mano([('10', ''), ('K', '')]), 20)

    def test_con_ases(self):
        self.assertEqual(valor_mano([('A', ''), ('9', '')]), 20)
        self.assertEqual(valor_mano([('A', ''), ('A', '')]), 12)
        self.assertEqual(valor_mano([('A', ''), ('K', '')]), 21)

    def test_busto(self):
        self.assertEqual(valor_mano([('10', ''), ('K', ''), ('5', '')]), 25)
    