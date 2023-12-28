from juego import Jugador, Estado 
import unittest


class TestEstado(unittest.TestCase):

    def setUp(self):
        jugador = Jugador()
        crupier = Jugador()
        self.estado = Estado(jugador, crupier, turno=0)

    def test_is_terminal(self):
        self.estado.jugador.actualizar_mano(('A', 'Picas'))
        self.estado.jugador.actualizar_mano(('K', 'Corazones'))
        self.assertTrue(self.estado.is_terminal())

    def test_determinar_ganador(self):
        self.estado.jugador.actualizar_mano(('K', 'Corazones'))
        self.estado.crupier.actualizar_mano(('9', 'Picas'))
        self.estado.determinar_ganador()
        self.assertEqual(self.estado.jugador.resultado, 'Gana')
