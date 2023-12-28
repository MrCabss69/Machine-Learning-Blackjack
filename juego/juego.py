import random

def valor_mano(mano):
    valor = sum(
        11 if c == 'A' else 10 if c in 'TJQK' else int(c) 
        for c, _ in mano 
    )
    ases = sum(1 for c, _ in mano if c == 'A')

    while valor > 21 and ases:
        valor -= 10
        ases -= 1

    return valor


class Jugador:
    
    def __init__(self):
        self.mano, self.apuesta = [], 1
        self.ultima_accion, self.resultado  = None, None

    def actualizar_mano(self, carta):
        self.mano.append(carta)

    def mostrar_mano(self):
        return ", ".join(f"{valor} de {palo}" for valor, palo in self.mano)
    

class Estado:
    
    def __init__(self, jugador, crupier, turno):
        self.jugador = jugador
        self.crupier = crupier 
        self.turno = turno
        self.cartas_jugador, self.cartas_crupier = self.jugador.mano, crupier.mano
        self.apuestas = self.jugador.apuesta
        

    def is_terminal(self):
        return valor_mano(self.cartas_jugador) >= 21 or valor_mano(self.cartas_crupier) >= 17
    
    def determinar_ganador(self):
        valor_crupier = valor_mano(self.cartas_crupier)
        valor_jugador = valor_mano(self.cartas_jugador)
        self.jugador.resultado = "Pierde" if valor_jugador > 21 or (valor_crupier <= 21 and valor_jugador < valor_crupier) else "Gana" if valor_crupier > 21 or valor_jugador > valor_crupier else "Empata"
    
    def get_available_actions(self):
        acciones = []
        cartas = self.cartas_jugador if self.turno == 0 else self.cartas_crupier
        valor_mano_jugador = valor_mano(cartas)

        if valor_mano_jugador < 21:
            acciones.append('HIT')
        acciones.append('STAND')
        return acciones

    
    
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
        for j in  [self.jugador, self.crupier]:
            j.actualizar_mano(self.baraja.pop())
            j.actualizar_mano(self.baraja.pop())
        self.actualiza_estado()

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
        self.actualiza_estado()

    def jugar_mano(self):
        self.init_hand()
        self.juega_jugador()  # El jugador juega primero

        # Si el turno sigue siendo del jugador, significa que se plantó y ahora es el turno del crupier
        if self.turno == 0:
            self.juega_crupier()

        self.determinar_ganador()  # Determinar el ganador al final del juego


    def actualiza_estado(self):
        self.estado = Estado(self.jugador, self.crupier, self.turno)

    def determinar_ganador(self):
        self.estado.determinar_ganador()

    def ejecutar_accion(self, accion):
        jugador_actual = self.jugador if self.turno == 0 else self.crupier
        if accion == 'HIT':
            jugador_actual.actualizar_mano(self.baraja.pop())
            self.actualiza_estado()
            if valor_mano(jugador_actual.mano) >= 21:
                self.cambia_turno()
        elif accion == 'STAND':
            self.cambia_turno()

    def cambia_turno(self):
        if self.turno == 0:
            self.turno = None
        else:
            self.turno = 0  