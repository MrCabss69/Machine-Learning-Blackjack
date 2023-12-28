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
    
    def __init__(self, jugadores, crupier, turno):
        self.jugadores = jugadores
        self.crupier = crupier 
        self.turno = turno
        self.cartas_jugadores, self.cartas_crupier = {j: j.mano for j in jugadores}, crupier.mano
        self.apuestas = {j: j.apuesta for j in jugadores}
        

    def is_terminal(self):
        return all(valor_mano(j.mano) >= 21 for j in self.cartas_jugadores) or valor_mano(self.cartas_crupier) >= 17
    
    def determinar_ganador(self):
        valor_crupier = valor_mano(self.cartas_crupier)
        for j in self.cartas_jugadores:
            valor_jugador = valor_mano(j.mano)
            j.resultado = "Pierde" if valor_jugador > 21 or (valor_crupier <= 21 and valor_jugador < valor_crupier) else "Gana" if valor_crupier > 21 or valor_jugador > valor_crupier else "Empata"
    
    def get_available_actions(self):
        acciones = []
        cartas = list(self.cartas_jugadores.values())[0] if self.turno == 0 else self.cartas_crupier
        valor_mano_jugador = valor_mano(cartas)

        if valor_mano_jugador < 21:
            acciones.append('HIT')
        acciones.append('STAND')
        return acciones

    
    
class Juego:
    
    def __init__(self, network, n_barajas=1):
        self.baraja = self.crear_baraja(n_barajas)
        self.jugadores = [Jugador()]
        self.crupier = Jugador()
        self.network = network
        self.turno = 0
        self.actualiza_estado()

    def crear_baraja(self, n_barajas):
        baraja = [(v, p) for v in '23456789TJQKA' for p in ['Corazones', 'Diamantes', 'Picas', 'Tréboles']] * n_barajas
        random.shuffle(baraja)
        return baraja

    def init_hand(self):
        for j in self.jugadores + [self.crupier]:
            j.actualizar_mano(self.baraja.pop())
            j.actualizar_mano(self.baraja.pop())
        self.actualiza_estado()

    def juega_jugador(self):
        jugador_actual = self.jugadores[self.turno]
        while valor_mano(jugador_actual.mano) < 21:
            accion = self.network.get_action(self.estado)
            jugador_actual.ultima_accion = accion
            self.ejecutar_accion(accion)
            if accion == 'STAND':
                break

    def juega_crupier(self):
        while valor_mano(self.crupier.mano) < 17:
            self.crupier.actualizar_mano(self.baraja.pop())
        self.actualiza_estado()

    def jugar_mano(self):
        self.init_hand()
        while self.turno is not None:
            self.juega_jugador()
            self.turno += 1
        self.juega_crupier()
        self.determinar_ganador()

    def actualiza_estado(self):
        self.estado = Estado(self.jugadores, self.crupier, self.turno)

    def determinar_ganador(self):
        self.estado.determinar_ganador()

    def ejecutar_accion(self, accion):
        jugador_actual = self.jugadores[self.turno] if self.turno < len(self.jugadores) else self.crupier
        if accion == 'HIT':
            jugador_actual.actualizar_mano(self.baraja.pop())
            self.actualiza_estado()
            if valor_mano(jugador_actual.mano) >= 21:
                self.cambia_turno()
        elif accion == 'STAND':
            self.cambia_turno()

    def cambia_turno(self):
        if self.turno < len(self.jugadores) - 1:
            self.turno += 1
        else:
            self.turno = None