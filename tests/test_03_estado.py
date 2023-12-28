from juego import Jugador, Estado 
import unittest

class TestEstado(unittest.TestCase):
    def setUp(self):
        self.jugadores = [Jugador(), Jugador()]
        self.crupier = Jugador()
        self.estado = Estado(self.jugadores, self.crupier)

    def test_is_terminal_false(self):
        # Asegurándose de que el juego no es terminal (nadie ha alcanzado o superado 21)
        self.jugadores[0].actualizar_mano(('10', 'Corazones'))
        self.jugadores[0].actualizar_mano(('2', 'Diamantes'))
        self.jugadores[1].actualizar_mano(('9', 'Picas'))
        self.jugadores[1].actualizar_mano(('2', 'Tréboles'))
        self.crupier.actualizar_mano(('7', 'Corazones'))
        self.crupier.actualizar_mano(('2', 'Diamantes'))
        self.assertFalse(self.estado.is_terminal())


    def test_is_terminal_true(self):
        # Configurando una situación donde el juego es terminal (todos los jugadores y el crupier han alcanzado o superado 21)
        for jugador in self.jugadores:
            jugador.actualizar_mano(('A', 'Corazones'))
            jugador.actualizar_mano(('K', 'Diamantes'))
        self.crupier.actualizar_mano(('T', 'Picas'))
        self.crupier.actualizar_mano(('7', 'Tréboles'))
        self.assertTrue(self.estado.is_terminal())


    def test_determinar_ganador(self):
        self.jugadores[0].actualizar_mano(('A', 'Corazones'))
        self.jugadores[0].actualizar_mano(('9', 'Diamantes'))
        self.jugadores[1].actualizar_mano(('K', 'Picas'))
        self.jugadores[1].actualizar_mano(('6', 'Tréboles'))
        self.crupier.actualizar_mano(('T', 'Corazones'))
        self.crupier.actualizar_mano(('6', 'Diamantes'))
        self.estado.determinar_ganador()
        self.assertEqual(self.jugadores[0].resultado, "Gana")
        self.assertEqual(self.jugadores[1].resultado, "Empata")