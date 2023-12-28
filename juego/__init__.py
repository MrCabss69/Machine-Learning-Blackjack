import random 
from .jugador import Jugador
from .estado import Estado, valor_mano


class Juego:
    
    def __init__(self, network, n_barajas=1):
        self.baraja = self.crear_baraja(n_barajas)
        self.jugador = Jugador()
        self.crupier = Jugador()
        self.network = network
        self.turno = 0
        self.actualiza_estado()

    def crear_baraja(self, n_barajas):
        baraja = [(v, p) for v in '23456789TJQKA' for p in ['Corazones', 'Diamantes', 'Picas', 'Tréboles']] * n_barajas
        random.shuffle(baraja)
        return baraja

    def init_hand(self):
        for j in [self.jugador, self.crupier]:
            j.actualizar_mano(self.baraja.pop())
            j.actualizar_mano(self.baraja.pop())
        self.actualiza_estado()
        print(f"Manos iniciales - Jugador: {self.jugador.mostrar_mano()}, Crupier: {self.crupier.mostrar_mano()}")

    def juega_jugador(self):
        while valor_mano(self.jugador.mano) < 21:
            accion = self.network.get_action(self.estado)
            self.jugador.ultima_accion = accion
            self.ejecutar_accion(accion)
            if accion == 'STAND':
                break

    def juega_crupier(self):
        while valor_mano(self.crupier.mano) < 17:
            self.crupier.actualizar_mano(self.baraja.pop())
            if self.estado.is_terminal():
                break
        self.actualiza_estado()

    def jugar_mano(self):
        self.init_hand()
        self.juega_jugador()
        if self.turno == 0:
            self.juega_crupier()
        self.determinar_ganador()
        print(f"Resultado del juego - Jugador: {self.jugador.resultado}")


    def actualiza_estado(self):
        self.estado = Estado(self.jugador, self.crupier, self.turno)

    def determinar_ganador(self):
        self.estado.determinar_ganador()

    def ejecutar_accion(self, accion):
        jugador_actual = self.jugador if self.turno == 0 else self.crupier
        print(f"Accion {accion} por {'Jugador' if self.turno == 0 else 'Crupier'}")
        if accion == 'HIT':
            jugador_actual.actualizar_mano(self.baraja.pop())
            self.actualiza_estado()
            print(f"Mano actual: {jugador_actual.mostrar_mano()}")
            if valor_mano(jugador_actual.mano) >= 21:
                self.cambia_turno()
        elif accion == 'STAND':
            self.cambia_turno()

    def cambia_turno(self):
        self.turno = 1 if self.turno == 0 else 0