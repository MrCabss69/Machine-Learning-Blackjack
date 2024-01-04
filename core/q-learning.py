

# EXAMPLE

def jugar_blackjack(episodios, agente):
    resultados = []
    for episodio in range(episodios):
        juego = Juego(agente)
        juego.jugar_mano()
        resultados.append(juego.guardar_resultados())
        for e0, e1, accion, res in resultados[-1]:
            estado = (tuple(e0), tuple(e1))
            accion_str = 'HIT' if accion == [1, 0] else 'STAND'
            nuevo_estado = None
            agente.update_q_table(estado, accion_str, res, nuevo_estado)
    
    return resultados

agente = QLearningAgent()
resultados = jugar_blackjack(1000, agente)
