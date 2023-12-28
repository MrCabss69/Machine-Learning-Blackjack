from juego import Jugador
import unittest

class TestJugador(unittest.TestCase):

    def setUp(self):
        self.jugador = Jugador()

    def test_inicializacion(self):
        self.assertEqual(self.jugador.mano, [])
        self.assertEqual(self.jugador.apuesta, 1)

    def test_actualizar_y_mostrar_mano(self):
        self.jugador.actualizar_mano(('K', 'Picas'))
        self.jugador.actualizar_mano(('A', 'Corazones'))
        self.assertIn('K de Picas', self.jugador.mostrar_mano())
        self.assertIn('A de Corazones', self.jugador.mostrar_mano())
