
class Jugador:
    
    def __init__(self):
        self.mano, self.apuesta = [], 1
        self.ultima_accion, self.resultado  = None, None

    def actualizar_mano(self, carta):
        self.mano.append(carta)
        print(f"Mano actualizada: {self.mostrar_mano()}")

    def mostrar_mano(self):
        return ", ".join(f"{valor} de {palo}" for valor, palo in self.mano)
    