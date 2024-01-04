from tensorflow.keras.models import load_model
import numpy as np
import random 
from juego import codificar_estado, valor_mano
from collections import defaultdict

class Agente:
    def get_action(self, estado):
        pass
    
class Crupier(Agente):
    def __init__(self):
        pass

    def get_action(self, estado):
        valor, is_soft = valor_mano(estado.cartas_crupier)
        if valor < 17 or (is_soft and valor == 17):
            return 'HIT'
        return 'STAND'

class DummyAgent(Agente):
    def __init__(self):
        pass

    def get_action(self, estado):
        actions = estado.get_available_actions()
        return random.choice(actions)


class NeuralNetworkAgent(Agente):
    def __init__(self, input_size, model_p = None):
        self.model = load_model('pretrained/dnn3_5000000.h5' if model_p is not None else model_p)
        self.input_size = input_size

    def preprocess_state(self, estado, accion):
        encoded_state  = codificar_estado(estado.cartas_jugador, estado.cartas_crupier)
        encoded_action = [1,0] if accion == 'HIT' else [0,1]
        encoded_input  = encoded_state + encoded_action
        return np.reshape(encoded_input, (1, self.input_size))
    
    def get_action(self, estado):
        # Procesar estados para HIT y STAND una vez
        hit_state  = self.preprocess_state(estado, 'HIT')
        stay_state = self.preprocess_state(estado, 'STAND')

        # Realizar predicciones una vez por acción
        prediction_HIT   = self.model.predict(hit_state)[0]
        prediction_STAND = self.model.predict(stay_state)[0]

        # Calcular el valor esperado (EV) de cada acción
        ev_HIT   = -prediction_HIT[0] + prediction_HIT[2]
        ev_STAND = -prediction_STAND[0] + prediction_STAND[2]
        
        # Elegir la acción con mayor EV
        if ev_HIT == ev_STAND:
            return random.choice(['HIT', 'STAND'])
        return 'HIT' if ev_HIT > ev_STAND else 'STAND'
    
    
class QLearningAgent(Agente):
    
    def __init__(self, alpha: float = 0.1, gamma: float = 0.9, epsilon: float = 0.1):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = defaultdict(lambda: {'HIT': 0, 'STAND': 0}) 

    def get_action(self, estado: str) -> str:
        """
        Elige una acción basada en una política epsilon-greedy.
        """
        if random.random() < self.epsilon:
            return random.choice(['HIT', 'STAND'])
        return max(self.q_table[estado], key=self.q_table[estado].get)

    def update_q_table(self, estado: str, accion: str, recompensa: float, nuevo_estado: str):
        """
        Actualiza la Q-table usando la fórmula de Q-learning.
        """
        max_future_q = max(self.q_table[nuevo_estado].values())
        current_q = self.q_table[estado][accion]
        new_q = (1 - self.alpha) * current_q + self.alpha * (recompensa + self.gamma * max_future_q)
        self.q_table[estado][accion] = new_q