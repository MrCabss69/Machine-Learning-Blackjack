
from juego import Juego
from core import DummyNetwork
import unittest

class TestJuego(unittest.TestCase):

    def setUp(self):
        self.juego = Juego(network=None)

    def test_creacion_baraja(self):
        self.assertEqual(len(self.juego.baraja), 52)
        self.assertIn(('A', 'Corazones'), self.juego.baraja)

    def test_init_hand(self):
        self.juego.init_hand()
        self.assertEqual(len(self.juego.jugador.mano), 2)
        self.assertEqual(len(self.juego.crupier.mano), 2)