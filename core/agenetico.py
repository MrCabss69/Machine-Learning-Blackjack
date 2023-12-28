import random
from juego import Juego
import matplotlib.pyplot as plt 
import seaborn as sns




def funcion_aptitud(estrategia, juegos=100): 
    # Evalúa la aptitud de una estrategia jugando un número de juegos.
    return sum(1 if juego.jugar_mano().jugadores[0].resultado == "Gana" else -1
                    for _ in range(juegos) for juego in [Juego(n_barajas=1, estrategia=estrategia)])

def seleccion_torneo(poblacion, aptitudes, n=2):
    # Selecciona individuos de una población mediante torneos.
    return [max(random.sample(list(zip(poblacion, aptitudes)), 2), key=lambda x: x[1])[0] for _ in range(n)]

def cruce(cromosoma1, cromosoma2): 
    # Cruza dos cromosomas para crear uno nuevo.
    return {key: cromosoma1[key] if random.random() < 0.5 else cromosoma2[key] for key in cromosoma1}

def mutacion(cromosoma, tasa_mutacion=0.1): 
    # Aplica mutaciones a un cromosoma.
    return {key: valor + random.choice([-1, 1]) * random.random() if random.random() < tasa_mutacion else valor
            for key, valor in cromosoma.items()}

def evolucionar(poblacion_inicial, num_generaciones=100): 
    # Evoluciona una población a lo largo de generaciones
    registro = RegistroEvolucion()
    poblacion = poblacion_inicial
    for _ in range(num_generaciones):
        aptitudes = [] # funcion_aptitud(Estrategia(cromosoma)) for cromosoma in poblacion]
        registro.registrar_generacion(aptitudes)
        nueva_poblacion = [mutacion(cruce(*seleccion_torneo(poblacion, aptitudes))) for _ in range(len(poblacion))]
        poblacion = nueva_poblacion
    return poblacion, registro




class Cromosoma:
    
    def __init__(self):
        self.umbral_hit = 17
        self.umbral_doblar = 10
        self.umbral_dividir = 8
        
        
        
        
class RegistroEvolucion:
    
    def __init__(self):
        self.historial_aptitudes = []
        self.mejor_aptitud_por_generacion = []
        self.promedio_aptitud_por_generacion = []

    def registrar_generacion(self, aptitudes):
        self.historial_aptitudes.append(aptitudes)
        self.mejor_aptitud_por_generacion.append(max(aptitudes))
        self.promedio_aptitud_por_generacion.append(sum(aptitudes) / len(aptitudes))
        
        
        
        
class VisualizadorEvolucion:
    
    def __init__(self, registro_evolucion):
        self.registro = registro_evolucion

    def plot_desempeno_por_generacion(self):
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.registro.historial_aptitudes)
        plt.title("Desempeño por Generación")
        plt.xlabel("Generación")
        plt.ylabel("Aptitud")
        plt.show()

    def plot_mejora_generacional(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.registro.promedio_aptitud_por_generacion, marker='o')
        plt.title("Mejora Generacional en Aptitud Promedio")
        plt.xlabel("Generación")
        plt.ylabel("Aptitud Promedio")
        plt.show()