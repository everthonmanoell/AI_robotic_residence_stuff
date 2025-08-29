from enum import Enum, auto


class Estados(Enum):
    TERREO = auto()
    TOPO = auto()
    PARADO = auto()
    SUBIR = auto()
    DESCER = auto()


class Elevador:
    def __init__(self):
        self.estado = 'PARADO'

    def escolha():
        pass

    def estados(estado: Estados, escolha: Estados):
        escolha_atual = escolha

        
        if estado == Estados.PARADO:
            if escolha_atual == Estados.SUBIR:
                estado = Estados.SUBIR
            elif escolha_atual == Estados.DESCER:
                estado = Estados.DESCER
            else:
                estado = Estados.PARADO

        elif estado == Estados.SUBIR:
            if escolha_atual == Estados.PARADO:
                estado = Estados.PARADO
            elif escolha_atual == Estados.DESCER:
                estado = Estados.DESCER
            else:
                estado = Estados.SUBIR

        elif estado == Estados.DESCER:
            if escolha_atual == Estados.PARADO:
                estado = Estados.PARADO
            elif escolha_atual == Estados.SUBIR:
                estado = Estados.SUBIR
            else:
                estado = Estados.DESCER

        return estado
    
if __name__ == '__main__':
    elevador = Elevador()
    
