"""Exemplo de implementação de estados declarativa"""

class Semaforo:
    def __init__(self):
        pass




estados = ['VERMELHO', 'VERDE', 'AMARELO']
transicoes = [
    #vermelho -> verde
    {
        'trigger': 'abrir',
        'source': 'VERMELHO',
        'dest': 'VERDE',
        
    },
    #verde -> amarelo
    {
        'trigger': 'alerta',
        'source': 'VERDE',
        'dest': 'AMARELO',
        
    },
    #amarelo -> vermelho
    {
        'trigger': 'fechar',
        'source': 'AMARELO',
        'dest': 'VERMELHO',
        
    },

]

s = Semaforo()


