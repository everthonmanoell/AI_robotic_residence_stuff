
from transitions import Machine


class Semaforo: 
    def on_enter_VERMELHO(self):
        print('Sinal acabou de se tornar VERMELHO')
    def on_enter_VERDE(self):
        print('Sinal acabou de se tornar VERDE')
    def on_enter_AMARELO(self):
        print('Sinal acabou de se tornar AMARELO')
    def on_exit_VERMELHO(self):
        print('Sinal vai deixar de ser VERMELHO')
    def on_exit_VERDE(self):
        print('Sinal vai deixar de ser VERDE')
    def on_exit_AMARELO(self):
        print('Sinal vai deixar de ser AMARELO')
    def abriu(self):
        print('Abriu o sinal, podem passar!')
    def amarelou(self):
        print('Vai fechar o sinal, bora parando galera...')
    def fechou(self):
        print('Fechou o sinal, agora parou!')

estados = ['VERMELHO', 'VERDE', 'AMARELO']
transicoes = [
    #vermelho -> verde
    {
        'trigger': 'abrir',
        'source': 'VERMELHO',
        'dest' : 'VERDE',
        'after' : 'abriu' #callback
    },
    #verde -> amarelo
    {
        'trigger': 'alerta',
        'source': 'VERDE',
        'dest' : 'AMARELO',
        'after' : 'amarelou'
    },
    #amarelo -> vermelho
    {
        'trigger': 'fechar',
        'source': 'AMARELO',
        'dest' : 'VERMELHO',
        'after' : 'fechou'
    }
]
semaforo = Semaforo()
# print(semaforo.__dict__)
maquina = Machine(
    model = semaforo,
    states = estados,
    transitions = transicoes,
    initial = 'VERMELHO'
)

# print(maquina)

# print(semaforo.state)
semaforo.abrir()
# print(semaforo.state)
semaforo.alerta()
# print(semaforo.state)
semaforo.fechar()
# print(semaforo.state)
# print(semaforo.__dict__)