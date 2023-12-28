def valor_mano(mano):
    valor = sum(
        11 if c == 'A' else 10 if c in 'TJQK' else int(c) 
        for c, _ in mano  # Asegúrate de desempacar correctamente la tupla (valor, palo)
    )
    ases = sum(1 for c, _ in mano if c == 'A')

    while valor > 21 and ases:
        valor -= 10
        ases -= 1

    return valor




def codificar_mano(mano):
    # Define la codificación para cada carta
    codificacion_cartas = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    # Inicializa un vector de ceros para todas las cartas
    vector_mano = [0] * 13
    for carta in mano:
        indice = codificacion_cartas[carta[0]]
        vector_mano[indice] += 1
    return vector_mano

def codificar_estado(jugadores, crupier):
    # Codifica las manos de todos los jugadores y del crupier
    estado_codificado = []
    for jugador in jugadores:
        estado_codificado.append(codificar_mano(jugador.mano))
    estado_codificado.append(codificar_mano(crupier.mano))
    return estado_codificado