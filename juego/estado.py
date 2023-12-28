
def valor_mano(mano):
    valor = sum(11 if c == 'A' else 10 if c in 'TJQK' else int(c)  for c, _ in mano)
    ases  = sum(1 for c, _ in mano if c == 'A')
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    return valor
    

class Estado:
    
    def __init__(self, jugador, crupier, turno):
        self.jugador = jugador
        self.crupier = crupier 
        self.turno = turno
        self.cartas_jugador, self.cartas_crupier = self.jugador.mano, crupier.mano
        self.apuestas = self.jugador.apuesta
            

    def is_terminal(self):
        condicion = (self.jugador.ultima_accion == 'STAND' and valor_mano(self.cartas_crupier) >= 17) or valor_mano(self.cartas_jugador) >= 21  or valor_mano(self.cartas_crupier) > 21
        print(f"Estado terminal: {condicion}")
        return condicion
    
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