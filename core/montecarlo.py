import matplotlib.pyplot as plt
from tqdm import tqdm
import pandas as pd
from juego import Juego

class MontecarloBlackjack:
    
    def __init__(self, agentes, n_simulaciones, save=True):
        self.agentes = agentes
        self.n_simulaciones = n_simulaciones
        self.resultados = {nombre: [] for nombre in agentes}
        self.save = save

    def simular(self):
        for nombre, agente in self.agentes.items():
            ganancias_acumuladas = 0
            historial_ganancias = []
            for _ in tqdm(range(self.n_simulaciones), desc=f"Simulando {nombre}"):
                juego = Juego(agente)
                juego.setup()
                while not juego.is_terminal():
                    if len(juego.baraja) < 5:
                        juego.baraja = juego.new_deck()
                        juego.actualizar_estado()
                    jugador_activo = juego.jugador_activo()
                    accion = agente.get_action(juego.estado)
                    if not accion:
                        print(juego.estado,'WRONG ACTION')
                    juego.realizar_accion(jugador_activo, accion)
                ganancia = self.calcular_ganancia(juego)
                ganancias_acumuladas += ganancia
                historial_ganancias.append(ganancias_acumuladas)
            self.resultados[nombre] = historial_ganancias
        if self.save:
            self.guardar_en_csv()

    def calcular_ganancia(self, juego):
        resultado = juego.get_resultados()
        return sum(res[-1] for res in resultado) if resultado else 0

    def guardar_en_csv(self):
        data_for_df = []
        for agente, ganancias in self.resultados.items():
            for i, ganancia in enumerate(ganancias):
                data_for_df.append([agente, i + 1, ganancia])
        df = pd.DataFrame(data_for_df, columns=['Agente', 'Juego', 'Ganancias Acumuladas'])
        df.to_csv(f'mc_{self.n_simulaciones}.csv', index=False)

    def plot_resultados(self):
        for nombre, historial in self.resultados.items():
            plt.plot(historial, label=nombre)
        plt.xlabel('Número de Juegos')
        plt.ylabel('Ganancias Acumuladas')
        plt.title('Comparación de Estrategias en Blackjack')
        plt.legend()
        plt.show()
