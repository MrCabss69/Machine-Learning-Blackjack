import random
from auxiliar import valor_mano

class Jugador:
    
    def __init__(self):
        self.mano, self.apuesta = [], 0
        self.ultima_accion, self.resultado  = None, None

    def actualizar_mano(self, carta):
        self.mano.append(carta)

    def mostrar_mano(self):
        return ", ".join(f"{valor} de {palo}" for valor, palo in self.mano)
    
    def copy(self):
        # Create a new instance of the Jugador class
        new_jugador = Jugador()

        # Copy the attributes of the original jugador instance to the new instance
        new_jugador.mano = self.mano.copy()
        new_jugador.apuesta = self.apuesta
        new_jugador.ultima_accion = self.ultima_accion
        new_jugador.resultado = self.resultado

        return new_jugador
    
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

    def copy(self):
        # Create a new instance of the Estado class
        new_estado = Estado(self.jugadores,self.crupier, self.turno)

        # Copy the attributes of the original estado instance to the new instance
        new_estado.cartas_jugadores = self.cartas_jugadores.copy()
        new_estado.cartas_crupier = self.cartas_crupier.copy()
        new_estado.apuestas = self.apuestas.copy()

        return new_estado
    
    
class Juego:
    
    def __init__(self, network, n_barajas = 1):
        self.baraja, self.jugadores, self.crupier, self.network = self.crear_baraja(n_barajas), [Jugador()], Jugador(), network
        self.turno = None
        self.actualiza_estado()
        
    def crear_baraja(self, n_barajas):
        baraja = [(v, p) for v in '23456789TJQKA' for p in ['Corazones', 'Diamantes', 'Picas', 'Tréboles']] * n_barajas
        random.shuffle(baraja)
        return baraja

    def jugar_mano(self):
        self.repartir_cartas_iniciales()
        self.turno = 0
        self.actualiza_estado()
        for j in self.jugadores: # get player policy network based
            while valor_mano(j.mano) < 21:
                accion = self.network.get_action(self.estado)
                j.ultima_accion = accion
                if accion == 'HIT':
                    j.actualizar_mano(self.baraja.pop())
                    self.actualiza_estado()
                elif accion == 'STAND':
                    break
            self.turno += 1
            self.actualiza_estado()
        self.crupier_juega()
        self.actualiza_estado()
        self.determinar_ganador()
        
    def copy(self):
        # Create a new instance of the Juego class
        new_juego = Juego(self.network)
        new_juego.baraja    = self.baraja.copy()
        new_juego.jugadores = self.jugadores.copy()
        new_juego.crupier   = self.crupier.copy()
        new_juego.turno     = self.turno
        new_juego.estado    = self.estado.copy()
        return new_juego

    def repartir_cartas_iniciales(self):
        for j in self.jugadores + [self.crupier]:
            j.actualizar_mano(self.baraja.pop()), j.actualizar_mano(self.baraja.pop())

    def crupier_juega(self):
        while valor_mano(self.crupier.mano) < 17:
            self.crupier.actualizar_mano(self.baraja.pop())
            
    def actualiza_estado(self):
        self.estado = Estado(self.jugadores, self.crupier, self.turno)
        
    def determinar_ganador(self):
        self.estado.determinar_ganador()
