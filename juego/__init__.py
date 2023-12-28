import random 
from .jugador import *
from .estado import  * 


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
        # print(f"Manos iniciales - Jugador: {self.jugador.mostrar_mano()}, Crupier: {self.crupier.mostrar_mano()}")

    def juega_jugador(self):
        valor, is_soft = valor_mano(self.jugador.mano)
        while valor < 21:
            accion = self.network.get_action(self.estado)
            self.jugador.ultima_accion = accion
            if accion == 'HIT':
                self.jugador.actualizar_mano(self.baraja.pop())
                valor, is_soft = valor_mano(self.jugador.mano)
                self.actualiza_estado()
            elif accion == 'STAND':
                self.turno = 1
                break
        # print(f"Mano final del jugador: {self.jugador.mostrar_mano()}")
        self.actualiza_estado()

    def juega_crupier(self):
        valor, is_soft = valor_mano(self.crupier.mano)
        while valor < 17 or (is_soft and valor == 17):
            self.crupier.actualizar_mano(self.baraja.pop())
            valor, is_soft = valor_mano(self.crupier.mano)
            self.actualiza_estado()
        # print(f"Mano final del crupier: {self.crupier.mostrar_mano()}")

    def jugar_mano(self):
        self.init_hand()
        self.juega_jugador()
        if self.turno == 1 and not self.estado.is_terminal():
            self.juega_crupier()
        self.estado.determinar_ganador()

    def actualiza_estado(self):
        self.estado = Estado(self.jugador, self.crupier, self.turno)
