import random
from juego import Juego

class QLearningAgent:
    def __init__(self, alpha, gamma, epsilon):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {} 

    def get_action(self, estado):
        if random.random() < self.epsilon:
            return random.choice(['HIT', 'STAND'])
        else:
            self.ensure_state_exists(estado)
            return max(self.q_table[estado], key=self.q_table[estado].get)

    def update_q_table(self, estado, accion, recompensa, nuevo_estado):
        self.ensure_state_exists(estado)
        self.ensure_state_exists(nuevo_estado)
        max_future_q = max(self.q_table[nuevo_estado].values())
        current_q = self.q_table[estado][accion]
        new_q = (1 - self.alpha) * current_q + self.alpha * (recompensa + self.gamma * max_future_q)
        self.q_table[estado][accion] = new_q

    def ensure_state_exists(self, estado):
        if estado not in self.q_table:
            self.q_table[estado] = {'HIT': 0, 'STAND': 0}

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

agente = QLearningAgent(alpha=0.1, gamma=0.9, epsilon=0.1)
resultados = jugar_blackjack(1000, agente)
