from juego import Jugador
import unittest

class TestJugador(unittest.TestCase):
    def setUp(self):
        self.jugador = Jugador()

    def test_inicializacion(self):
        self.assertEqual(self.jugador.mano, [])
        self.assertEqual(self.jugador.apuesta, 0)
        self.assertIsNone(self.jugador.resultado)

    def test_actualizar_mano(self):
        self.jugador.actualizar_mano(('A', 'Corazones'))
        self.assertIn(('A', 'Corazones'), self.jugador.mano)

    def test_mostrar_mano(self):
        self.jugador.actualizar_mano(('A', 'Corazones'))
        self.assertEqual(self.jugador.mostrar_mano(), "A de Corazones")
