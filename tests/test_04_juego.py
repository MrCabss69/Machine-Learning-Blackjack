
from juego import Juego, Jugador
from core import DummyNetwork
import unittest

class TestJuego(unittest.TestCase):

    def test_new_deck(self):
        juego = Juego(DummyNetwork())
        baraja = juego.new_deck(1)
        self.assertEqual(len(baraja), 52)
        self.assertIn(('A', 'Corazones'), baraja)
        self.assertIn(('K', 'Picas'), baraja)

    def test_deal(self):
        juego = Juego(DummyNetwork())
        juego.setup()
        self.assertEqual(len(juego.jugador.mano), 2)
        self.assertEqual(len(juego.crupier.mano), 2)
        self.assertEqual(len(juego.baraja), 52 - 4)

    def test_realizar_accion_hit(self):
        juego = Juego(DummyNetwork())
        juego.baraja = juego.new_deck()
        juego.jugador = Jugador()
        juego.crupier = Jugador()
        juego.jugador.actualizar_mano(('2', 'Corazones'))
        juego.jugador.actualizar_mano(('9', 'Picas'))
        juego.actualizar_estado()
        juego.realizar_accion(juego.jugador, 'HIT')

    def test_realizar_accion_stand(self):
        juego = Juego(DummyNetwork())
        juego.jugador = Jugador()
        juego.crupier = Jugador()
        juego.jugador.actualizar_mano(('K', 'Corazones'))
        juego.jugador.actualizar_mano(('K', 'Picas'))
        juego.actualizar_estado()
        juego.realizar_accion(juego.jugador, 'STAND')
        self.assertEqual(juego.turno, 1)

    def test_is_terminal(self):
        juego = Juego(DummyNetwork())
        juego.jugador = Jugador()
        juego.crupier = Jugador()
        juego.jugador.actualizar_mano(('A', 'Corazones'))
        juego.jugador.actualizar_mano(('K', 'Picas'))
        juego.actualizar_estado()
        self.assertTrue(juego.is_terminal())

    def test_determinar_ganador(self):
        juego = Juego(DummyNetwork())
        juego.jugador = Jugador()
        juego.crupier = Jugador()
        juego.jugador.actualizar_mano(('10', 'Corazones'))
        juego.jugador.actualizar_mano(('K', 'Picas'))
        juego.crupier.actualizar_mano(('7', 'Diamantes'))
        juego.crupier.actualizar_mano(('K', 'Picas'))
        juego.actualizar_estado()
        resultado = juego.estado.determinar_ganador()
        self.assertEqual(resultado, 1)

    def test_get_available_actions(self):
        juego = Juego(DummyNetwork())
        juego.setup()
        self.assertIn('HIT', juego.acciones_posibles())
        self.assertIn('STAND', juego.acciones_posibles())

if __name__ == '__main__':
    unittest.main()
