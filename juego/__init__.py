import random 
from .jugador import *
from .estado import  *

class Juego:
    
    def __init__(self, network):
        self.network = network
        self.estado  = None
        self.jugador = None
        self.crupier = None
        self.historial = []
        self.turno     = 0
        self.baraja    = []
    
    def get_estado(self):
        self.actualizar_estado()
        return self.estado

    def new_deck(self, n=1):
        baraja = [(v, p) for v in '23456789TJQKA' for p in ['Corazones', 'Diamantes', 'Picas', 'Tréboles']] * n
        random.shuffle(baraja)
        return baraja

    def deal(self):
        if not self.baraja or len(self.baraja) < 4:
            raise ValueError("Baraja insuficiente para repartir cartas.")
        for j in [self.jugador, self.crupier]:
            j.actualizar_mano(self.baraja.pop())
            j.actualizar_mano(self.baraja.pop())
    
    def setup(self):
        self.jugador = Jugador()
        self.crupier = Jugador()
        self.historial = []
        self.turno = 0
        self.baraja = self.new_deck()
        self.deal()
        self.actualizar_estado()

    def actualizar_estado(self):
        self.estado = Estado(self.jugador, self.crupier, self.turno)
        if self.jugador.ultima_accion:
            accion = [1, 0] if self.jugador.ultima_accion == 'HIT' else [0, 1]
            estado_actual = codificar_estado(self.jugador.mano, self.crupier.mano)
            self.historial.append([estado_actual, accion])

    def is_terminal(self):
        return self.estado is not None and self.estado.is_terminal()

    def acciones_posibles(self):
        print(f"Estado terminal: {self.is_terminal()}, Acciones disponibles: {self.estado.get_available_actions()}")
        if self.is_terminal():
            return []
        return self.estado.get_available_actions()

    def realizar_accion(self, jugador_activo, accion):
        print(f"Acciones posibles: {self.acciones_posibles()}, Acción intentada: {accion}")
        if accion not in self.acciones_posibles():
            raise ValueError("Acción inválida")
        if accion == 'HIT':
            jugador_activo.actualizar_mano(self.baraja.pop())
        elif accion == 'STAND':
            jugador_activo.ultima_accion = 'STAND'
            self.turno = 1 - self.turno
        self.actualizar_estado()

    def jugador_activo(self):
        return self.jugador if self.turno == 0 else self.crupier

    def get_resultados(self):
        resultado = self.estado.determinar_ganador()
        self.actualizar_estado()
        if self.historial != []:
            return [[e0, accion, resultado] for e0, accion in self.historial] if self.historial else []
