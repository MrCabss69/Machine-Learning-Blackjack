import pandas as pd
from juego import Juego
from tqdm import tqdm
from .agentes import DummyAgent

class SimulacionMontecarlo:
    
    def __init__(self, n_barajas, n_simulaciones):
        self.n_barajas = n_barajas
        self.n_simulaciones = n_simulaciones
        self.resultados = []
        self.estadisticas = {'ganadas': 0,'perdidas': 0,'empates': 0}

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
        columns_ = ['Mano Jugador', 'Mano Crupier', 'Accion', 'Resultado']
        df = pd.DataFrame(self.resultados, columns=columns_)
        df_estadisticas = pd.DataFrame([self.estadisticas])
        df.to_csv(f'mc_{self.n_simulaciones}.csv', index=False)
        df_estadisticas.to_csv(f'stats_mc_{self.n_simulaciones}.csv')