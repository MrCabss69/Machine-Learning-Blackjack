from unittest.mock import MagicMock
from juego import Juego 
from auxiliar import valor_mano
import unittest


class TestJuego(unittest.TestCase):
    def setUp(self):
        self.network = MagicMock()
        self.juego = Juego(self.network)

    def test_init(self):
        self.assertEqual(len(self.juego.baraja), 52)
        self.assertEqual(len(self.juego.jugadores), 1)
        self.assertIsNotNone(self.juego.crupier)

    def test_crear_baraja(self):
        baraja = self.juego.crear_baraja(1)
        self.assertEqual(len(baraja), 52)

    def test_jugar_mano(self):
        self.network.get_action.return_value = 'STAND'
        self.juego.repartir_cartas_iniciales()
        self.juego.jugar_mano()
        # Añadir aserciones para verificar el estado después de jugar una mano, como por ejemplo:
        for jugador in self.juego.jugadores:
            self.assertTrue(valor_mano(jugador.mano) >= 21 or self.network.get_action.called)

    def test_repartir_cartas_iniciales(self):
        self.juego.repartir_cartas_iniciales()
        for jugador in self.juego.jugadores + [self.juego.crupier]:
            self.assertEqual(len(jugador.mano), 2)

    def test_crupier_juega(self):
        self.juego.crupier.actualizar_mano(('5', 'Corazones'))
        self.juego.crupier_juega()
        self.assertTrue(valor_mano(self.juego.crupier.mano) >= 17)
