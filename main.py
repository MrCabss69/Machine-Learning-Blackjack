from core import DummyNetwork
from juego import Juego

if __name__ == "__main__":
    juego = Juego( DummyNetwork())
    for _ in range(5):
        juego.jugar_mano()
        print("Resultados de la mano:")
        for jugador in juego.jugadores:
            print(f"Jugador: {jugador.mostrar_mano()}, Resultado: {jugador.resultado}")