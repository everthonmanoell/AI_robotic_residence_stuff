from enum import Enum
class EstadosElevador(Enum):
    PARADO = 1
    SUBINDO = 6
    DESCENDO = 7
    ABRINDO_PORTAS = 11
    FECHANDO_PORTAS = 12
class Elevador:
    def __init__(self):
        self.estado = "PARADO"

    def subir(self) -> bool:
        if self.estado in {"PARADO"}:
            self.estado = "SUBINDO"
            return True
        return False  # já está subindo ou descendo

    def descer(self) -> bool:
        if self.estado in {"PARADO"}:
            self.estado = "DESCENDO"
            return True
        return False  

    def parar(self) -> bool:
        if self.estado in {"SUBINDO", "DESCENDO"}:
            self.estado = "PARADO"
            return True
        return False  
    
if __name__=='__main__':
    e = Elevador()
    print(e.estado)   
    e.subir()
    print(e.estado)   
    #e.parar()
    e.descer()

    print(e.estado)   
    e.descer()
    print(e.estado)   
