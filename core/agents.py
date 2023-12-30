from tensorflow.keras.models import load_model
import numpy as np
import random 
from juego import codificar_estado


class DummyAgent:
    def __init__(self, estrategia=None):
        self.estrategia = estrategia

    def get_action(self, estado):
        if self.estrategia and callable(self.estrategia):
            return self.estrategia(estado)
        actions = estado.get_available_actions()
        return random.choice(actions)


class NeuralNetworkAgent:
    def __init__(self, input_size, model_p = None):
        self.model = load_model('pretrained/dnn3_5000000.h5' if model_p is not None else model_p)
        self.input_size = input_size

    def preprocess_state(self, estado, accion):
        encoded_state = codificar_estado(estado.cartas_jugador, estado.cartas_crupier)
        encoded_action = [1,0] if accion == 'HIT' else [0,1]
        encoded_input = encoded_state + encoded_action
        return np.reshape(encoded_input, (1, self.input_size))
    
    def get_action(self, estado):
        # Procesar estados para HIT y STAND una vez
        hit_state = self.preprocess_state(estado, 'HIT')
        stay_state = self.preprocess_state(estado, 'STAND')

        # Realizar predicciones una vez por acción
        prediction_HIT = self.model.predict(hit_state)[0]
        prediction_STAND = self.model.predict(stay_state)[0]

        # Calcular el valor esperado (EV) de cada acción
        ev_HIT = -prediction_HIT[0] + prediction_HIT[2]
        ev_STAND = -prediction_STAND[0] + prediction_STAND[2]
        
        # Elegir la acción con mayor EV
        if ev_HIT == ev_STAND:
            return random.choice(['HIT', 'STAND'])
        return 'HIT' if ev_HIT > ev_STAND else 'STAND'