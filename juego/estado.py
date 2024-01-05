def valor_mano(mano):
    valor, ases = 0, 0
    for carta, _ in mano:
        if carta == 'A':
            valor += 11
            ases += 1
        else:
            valor += 10 if carta in 'TJQK' else int(carta)
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    soft = ases > 0
    return valor, soft


def codificar_mano(mano):
    codificacion_cartas = {
        '2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 
        'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12
    }
    return [sum(card[0] == rank for card in mano) for rank in codificacion_cartas.keys()]


def codificar_estado(mano_jugador, mano_crupier):
    jugador = codificar_mano(mano_jugador)
    crupier = codificar_mano(mano_crupier)
    return jugador + crupier


class Estado:
    def __init__(self, jugador, crupier, turno):
        self.jugador = jugador
        self.crupier = crupier
        self.turno = turno
        self.cartas_jugador = jugador.mano
        self.cartas_crupier = crupier.mano

    def is_terminal(self):
        valor_crupier, _ = valor_mano(self.cartas_crupier)
        valor_jugador, _ = valor_mano(self.cartas_jugador)
        blackjack_jugador = valor_jugador == 21 and len(self.cartas_jugador) == 2
        blackjack_crupier = valor_crupier == 21 and len(self.cartas_crupier) == 2
        return (
            blackjack_jugador or blackjack_crupier or valor_crupier >= 17 or 
            valor_jugador >= 21 or valor_crupier >= 21
        )

    def determinar_ganador(self):
        if not self.is_terminal():
            raise ValueError("No se puede determinar el ganador antes de que el juego termine.")
        valor_crupier, _ = valor_mano(self.cartas_crupier)
        valor_jugador, _ = valor_mano(self.cartas_jugador)
        if valor_jugador > 21 or (valor_crupier <= 21 and valor_jugador < valor_crupier):
            self.jugador.resultado = -1
        elif valor_crupier > 21 or valor_jugador > valor_crupier:
            self.jugador.resultado = 1
        else:
            self.jugador.resultado = 0
        print(f"Valor jugador: {valor_jugador}, Valor crupier: {valor_crupier}, Resultado: {self.jugador.resultado}")

        return self.jugador.resultado

    def get_available_actions(self):
        
        activo = self.jugador if self.turno == 0 else self.crupier
        valor_actual_mano, is_soft_hand = valor_mano(activo.mano)
        if activo.ultima_accion == 'STAND' or self.is_terminal():
            return []
        acciones = ['STAND']
        if valor_actual_mano < 21 or (is_soft_hand and valor_actual_mano <= 21):
            acciones.insert(0, 'HIT')
        return acciones

    def get_estado_codificado(self):
        return codificar_estado(self.cartas_jugador, self.cartas_crupier)

    def __str__(self):
        estado_str = "Estado del Juego de Blackjack\n"
        estado_str += "Estado codificado: " + str(self.get_estado_codificado()) + "\n"
        estado_str += "Turno: " + str(self.turno) + "\n"
        estado_str += "Mano del Jugador: " + str(self.cartas_jugador) + "\n"
        estado_str += "Mano del Crupier: " + str(self.cartas_crupier) + "\n"
        estado_str += "Acciones Disponibles: " + str(self.get_available_actions())
        return estado_str
