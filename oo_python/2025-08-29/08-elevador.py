from enum import Enum, auto
from transitions import Machine

class EstadoElevador(Enum):
    PARADO = auto()
    SUBINDO = auto()
    DESCENDO = auto()

class Elevador:
    def __init__(self):
        self.andar = 0
        self.machine = Machine(model=self, states=EstadoElevador, initial=EstadoElevador.PARADO)

        self.machine.add_transition("subir",  EstadoElevador.PARADO, EstadoElevador.SUBINDO)
        self.machine.add_transition("descer", EstadoElevador.PARADO,  EstadoElevador.DESCENDO)
        self.machine.add_transition("parar",  EstadoElevador.SUBINDO, EstadoElevador.PARADO)
        self.machine.add_transition("parar",  EstadoElevador.DESCENDO, EstadoElevador.PARADO)

    def tick(self):
        if self.state == EstadoElevador.SUBINDO:
            self.andar += 1
        elif self.state == EstadoElevador.DESCENDO:
            self.andar -= 1
if __name__ == "__main__":
    e = Elevador()
    print(e.state, e.andar)  
    e.subir()
    print(e.state, e.andar)  
    e.tick()
    print(e.state, e.andar)
    e.parar()
    print(e.state, e.andar)
    e.descer()
    print(e.state, e.andar)
    e.tick()
    e.tick()
    e.tick()
    print(e.state, e.andar)
    e.parar()
    print(e.state, e.andar)
