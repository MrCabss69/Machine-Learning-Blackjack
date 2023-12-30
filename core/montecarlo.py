import random
import pandas as pd
from juego import Juego
from tqdm import tqdm
from .agents import DummyAgent


def codificar_mano(mano):
    codificacion_cartas = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    return [sum(card[0] == rank for card in mano) for rank in codificacion_cartas]

def codificar_estado_inicial(estado):
    return [codificar_mano(estado.cartas_jugador[:2]), codificar_mano(estado.cartas_crupier[:1])]

class SimulacionMontecarlo:
    
    def __init__(self, n_barajas, n_simulaciones):
        self.n_barajas = n_barajas
        self.n_simulaciones = n_simulaciones
        self.resultados = []
        self.estadisticas = {
            'ganadas': 0,
            'perdidas': 0,
            'empates': 0
        }

    def simular(self):
        for _ in tqdm(range(self.n_simulaciones)):
            juego = Juego(DummyAgent(), n_barajas=self.n_barajas)
            juego.jugar_mano()
            resultado_mano = juego.guardar_resultados()
            self.resultados.extend(resultado_mano)
            self.actualizar_estadisticas(resultado_mano)
        self.guardar_en_csv()

    def actualizar_estadisticas(self, resultado_mano):
        for _, _, _, resultado in resultado_mano:
            if resultado == 1:
                self.estadisticas['ganadas'] += 1
            elif resultado == -1:
                self.estadisticas['perdidas'] += 1
            else:
                self.estadisticas['empates'] += 1

    def guardar_en_csv(self):
        df = pd.DataFrame(self.resultados, columns=['Mano Jugador', 'Mano Crupier', 'Accion', 'Resultado'])
        df_estadisticas = pd.DataFrame([self.estadisticas])
        df_total = pd.concat([df, df_estadisticas], axis=1)
        df_total.to_csv(f'mc_{self.n_simulaciones}.csv', index=False)

# Uso de la clase SimulacionMontecarlo
simulador = SimulacionMontecarlo(n_barajas=1, n_simulaciones=1000)
simulador.simular()



