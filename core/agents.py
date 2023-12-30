from tensorflow.keras.models import load_model
import numpy as np
import random 


def codificar_mano(mano):
    codificacion_cartas = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    return [sum(card[0] == rank for card in mano) for rank in codificacion_cartas]

def codificar_estado(mano_jugador, mano_crupier):
    jugador = codificar_mano(mano_jugador)
    crupier = codificar_mano(mano_crupier)
    return jugador + crupier

def codificar_accion(accion):
    if accion == 'HIT':
        return [1, 0]
    elif accion == 'STAND':
        return [0, 1]
    else:
        raise ValueError("Acción no reconocida")



class DummyAgent:
    def __init__(self, estrategia=None):
        self.estrategia = estrategia

    def get_action(self, estado):
        if self.estrategia and callable(self.estrategia):
            return self.estrategia(estado)
        actions = estado.get_available_actions()
        return random.choice(actions)


class NeuralNetworkAgent:
    def __init__(self, input_size):
        model_path = 'pretrained/dnn3_5000000.h5'
        self.model = load_model(model_path)
        self.input_size = input_size

    def preprocess_state(self, estado, accion):
        encoded_state = codificar_estado(estado.cartas_jugador, estado.cartas_crupier)
        encoded_action = codificar_accion(accion)
        encoded_input = encoded_state + encoded_action
        if len(encoded_input) != self.input_size:
            raise ValueError(f"El tamaño del estado codificado {len(encoded_input)} no coincide con el tamaño de entrada esperado {self.input_size}.")
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
        if ev_HIT > ev_STAND:
            return 'HIT'
        elif ev_HIT < ev_STAND:
            return 'STAND'
        else:
            # Si los EV son iguales, elegir al azar
            return random.choice(['HIT', 'STAND'])