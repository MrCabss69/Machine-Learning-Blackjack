def valor_mano(mano):
    valor, ases, soft_ = 0, 0, False
    for carta, _ in mano:
        if carta == 'A':
            valor += 11
            ases += 1
        else:
            valor += 10 if carta in 'TJQK' else int(carta)
    if ases and valor <= 21:
        soft_ = True
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    return valor, soft_


class Estado:
    
    def __init__(self, jugador, crupier, turno):
        self.jugador = jugador
        self.crupier = crupier 
        self.turno = turno
        self.cartas_jugador = jugador.mano
        self.cartas_crupier = crupier.mano
        self.apuestas = jugador.apuesta

    def is_terminal(self):
        valor_crupier, soft_crupier_ = valor_mano(self.cartas_crupier)
        valor_jugador, _             = valor_mano(self.cartas_jugador)
        if self.jugador.ultima_accion == 'STAND' and (valor_crupier >= 17 and not soft_crupier_):
            return True
        return valor_jugador >= 21 or valor_crupier >= 21
    
    def determinar_ganador(self):
        valor_crupier, _ = valor_mano(self.cartas_crupier)
        valor_jugador, _ = valor_mano(self.cartas_jugador)
        if valor_jugador > 21 or (valor_crupier <= 21 and valor_jugador < valor_crupier):
            self.jugador.resultado = -1
        elif valor_crupier > 21 or valor_jugador > valor_crupier:
            self.jugador.resultado = 1
        else:
            self.jugador.resultado = 0
    
    def get_available_actions(self):
        activo = self.jugador if self.turno == 0 else self.crupier
        cartas = activo.mano
        valor_actual_mano, is_soft_hand = valor_mano(cartas)
        if activo.ultima_accion == 'STAND':
            return []
        acciones = ['STAND']
        if valor_actual_mano < 21 or (is_soft_hand and valor_actual_mano <= 21):
            acciones.insert(0, 'HIT')
        return acciones
