import random
from juego import Juego 
import copy 


def codificar_mano(mano):
    # Define la codificación para cada carta
    codificacion_cartas = {'2': 0, '3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12}
    vector_mano = [0] * 13
    for carta in mano:
        indice = codificacion_cartas[carta[0]]
        vector_mano[indice] += 1
    return vector_mano

def codificar_estado(estado):
    # Codifica las manos de todos los jugadores y del crupier utilizando el objeto Estado
    return [ codificar_mano(estado.cartas_jugador), codificar_mano(estado.cartas_crupier) ]


class DummyNetwork:
    def get_action(self, estado):
        actions = estado.get_available_actions()
        return random.choice(actions)


class SimulacionMontecarlo:
    def __init__(self, n_barajas, n_simulaciones, n_simulaciones_intermedias):
        self.n_barajas = n_barajas
        self.n_simulaciones = n_simulaciones
        self.n_simulaciones_intermedias = n_simulaciones_intermedias
        self.resultados = []

    def simular(self):
        for i in range(self.n_simulaciones):
            print(f"Simulación {i+1} de {self.n_simulaciones}")
            juego = Juego(DummyNetwork())
            juego.init_hand()
            juego.jugar_mano()
            resultado = juego.jugador.resultado
            print(resultado,'\n')
            self.guardar_resultado(juego)

    def guardar_resultado(self, juego):
        jugador = juego.jugador
        estado_juego = codificar_estado(juego.estado)
        accion = [1,0] if jugador.ultima_accion == 'HIT' else [0,1]
        res = 1 if jugador.resultado == 'Gana' else -1 if jugador.resultado == 'Pierde' else 0
        print(f"Guardando resultado: {estado_juego}, Accion: {accion}, Resultado: {res}")
        self.resultados.append([estado_juego, accion, res])
