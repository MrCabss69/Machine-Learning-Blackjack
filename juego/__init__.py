import random 
from .jugador import *
from .estado import  * 


def codificar_mano(mano):
    codificacion_cartas = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    return [sum(card[0] == rank for card in mano) for rank in codificacion_cartas]

def codificar_estado(mano_jugador, mano_crupier):
    jugador = codificar_mano(mano_jugador)
    crupier = codificar_mano(mano_crupier)
    return jugador + crupier

def codificar_accion(accion):
    if accion == 'HIT':
        return [1, 0]
    elif accion == 'STAND':
        return [0, 1]
    else:
        raise ValueError("Acción no reconocida")


class Juego:
    
    def __init__(self, network, n_barajas=1):
        self.baraja    = self.crear_baraja(n_barajas)
        self.jugador   = Jugador()
        self.crupier   = Jugador()
        self.network   = network
        self.turno     = 0
        self.historial = []
        self.actualiza_estado(False)

    def crear_baraja(self, n_barajas):
        baraja = [(v, p) for v in '23456789TJQKA' for p in ['Corazones', 'Diamantes', 'Picas', 'Tréboles']] * n_barajas
        random.shuffle(baraja)
        return baraja

    def init_hand(self):
        for j in [self.jugador, self.crupier]:
            j.actualizar_mano(self.baraja.pop())
            j.actualizar_mano(self.baraja.pop())
        self.actualiza_estado()

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
        self.actualiza_estado()

    def juega_crupier(self):
        valor, is_soft = valor_mano(self.crupier.mano)
        while valor < 17 or (is_soft and valor == 17):
            self.crupier.actualizar_mano(self.baraja.pop())
            valor, is_soft = valor_mano(self.crupier.mano)
            self.actualiza_estado()

    def jugar_mano(self):
        self.init_hand()
        self.juega_jugador()
        if self.turno == 1 and not self.estado.is_terminal():
            self.juega_crupier()
        self.estado.determinar_ganador()

    def actualiza_estado(self,not_init_=True):
        self.estado = Estado(self.jugador, self.crupier, self.turno)
        if not_init_:
            estado_actual = codificar_estado(self.jugador.mano, self.crupier.mano)
            accion = [1, 0] if self.jugador.ultima_accion == 'HIT' else [0, 1]
            self.historial.append([estado_actual[0], estado_actual[1], accion])

    def guardar_resultados(self):
        res = 1 if self.jugador.resultado == 'Gana' else -1 if self.jugador.resultado == 'Pierde' else 0
        return [[e0, e1, accion, res] for e0, e1, accion in self.historial]
