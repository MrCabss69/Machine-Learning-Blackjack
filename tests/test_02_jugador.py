import unittest
from juego import Jugador, valor_mano

class TestJugador(unittest.TestCase):

    def test_inicializacion_jugador(self):
        jugador = Jugador()
        self.assertEqual(jugador.mano, [])
        self.assertEqual(jugador.apuesta, 1)  # Asumiendo que la apuesta inicial es 1

    def test_actualizar_mano(self):
        jugador = Jugador()
        jugador.actualizar_mano(('A', 'Picas'))
        self.assertIn(('A', 'Picas'), jugador.mano)
        self.assertEqual(len(jugador.mano), 1)

    def test_mostrar_mano(self):
        jugador = Jugador()
        jugador.actualizar_mano(('A', 'Picas'))
        self.assertEqual(jugador.mostrar_mano(), "A de Picas")

    def test_valor_mano(self):
        jugador = Jugador()
        jugador.actualizar_mano(('A', 'Picas'))
        jugador.actualizar_mano(('J', 'Diamantes'))
        valor, soft = valor_mano(jugador.mano)  # Asumiendo que valor_mano es un método de Jugador
        self.assertEqual(valor, 21)
        self.assertTrue(soft)

if __name__ == '__main__':
    unittest.main()
