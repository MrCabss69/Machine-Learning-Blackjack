import random
import json 
import pandas as pd
from juego import Juego
from tqdm import tqdm

def codificar_mano(mano):
    codificacion_cartas = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    return [sum(card[0] == rank for card in mano) for rank in codificacion_cartas]

def codificar_estado_inicial(estado):
    return [codificar_mano(estado.cartas_jugador[:2]), codificar_mano(estado.cartas_crupier[:1])]


class DummyNetwork:
    def get_action(self, estado):
        actions = estado.get_available_actions()
        return random.choice(actions)

class SimulacionMontecarlo:
    
    def __init__(self, n_barajas, n_simulaciones):
        self.n_barajas = n_barajas
        self.n_simulaciones = n_simulaciones
        self.resultados = []

    def simular(self):
        for _ in tqdm(range(self.n_simulaciones)):
            juego = Juego(DummyNetwork())
            juego.jugar_mano()
            self.guardar_resultado(juego)
        self.guardar_en_csv()

    def guardar_resultado(self, juego):
        jugador = juego.jugador
        estado_juego = codificar_estado_inicial(juego.estado)
        res = 1 if jugador.resultado == 'Gana' else -1 if jugador.resultado == 'Pierde' else 0
        accion = [1, 0] if jugador.ultima_accion == 'HIT' else [0, 1]
        accion_str = json.dumps(accion)

        # print(f"Guardando resultado: Mano del jugador: {estado_juego[0]}, Mano del crupier: {estado_juego[1]}, Accion: {accion_str}, Resultado: {res}\n")
        self.resultados.append([json.dumps(estado_juego[0]),json.dumps(estado_juego[1]), accion_str, res])

    def guardar_en_csv(self):
        df = pd.DataFrame(self.resultados, columns=['Mano Jugador','Mano Crupier', 'Accion', 'Resultado'])
        df.to_csv('resultados_blackjack.csv', index=False)