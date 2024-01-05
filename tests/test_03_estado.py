import unittest
from juego import Estado, Jugador

class TestEstado(unittest.TestCase):

    def test_is_terminal_con_21(self):
        jugador = Jugador()
        crupier = Jugador()
        jugador.actualizar_mano(('A', 'Picas'))
        jugador.actualizar_mano(('K', 'Diamantes'))
        estado = Estado(jugador, crupier, turno=0)
        self.assertTrue(estado.is_terminal())

    def test_determinar_ganador_jugador_gana(self):
        jugador = Jugador()
        crupier = Jugador()
        jugador.actualizar_mano(('A', 'Picas'))
        jugador.actualizar_mano(('K', 'Diamantes'))
        crupier.actualizar_mano(('K', 'Corazones'))
        crupier.actualizar_mano(('9', 'Tréboles'))
        estado = Estado(jugador, crupier, turno=0)
        ganador = estado.determinar_ganador()
        self.assertEqual(ganador, 1)

    def test_get_available_actions(self):
        jugador = Jugador()
        crupier = Jugador()
        jugador.actualizar_mano(('5', 'Picas'))
        jugador.actualizar_mano(('6', 'Diamantes'))
        estado = Estado(jugador, crupier, turno=0)
        
        self.assertIn('HIT', estado.get_available_actions())

if __name__ == '__main__':
    unittest.main()
