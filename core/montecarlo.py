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
    estado_codificado = []
    for jugador in estado.cartas_jugadores.values():
        estado_codificado.append(codificar_mano(jugador))
    estado_codificado.append(codificar_mano(estado.cartas_crupier))
    return estado_codificado



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
        for _ in range(self.n_simulaciones):
            juego = Juego(DummyNetwork())
            self.simular_juego(juego)

    def simular_juego(self, juego, es_intermedio=False):
        if juego.estado.is_terminal() or es_intermedio:
            self.guardar_resultado(juego)
            return

        acciones = juego.estado.get_available_actions()
        for accion in acciones:
            juego_copia = copy.deepcopy(juego)
            juego_copia.ejecutar_accion(accion)
            for _ in range(self.n_simulaciones_intermedias):
                self.simular_juego(juego_copia, es_intermedio=True)

    def guardar_resultado(self, juego):
        for jugador in juego.jugadores:
            estado_juego = codificar_estado(juego.estado)
            accion = [1,0] if jugador.ultima_accion == 'HIT' else [0,1]
            if jugador.resultado == 'Gana':
                res = 1
            elif jugador.resultado == 'Pierde':
                res = -1 
            else:
                res = 0
            self.resultados.append([estado_juego, accion, res])

