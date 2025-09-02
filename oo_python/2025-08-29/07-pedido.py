from transitions import Machine

class Pedido:
    def __init__(self, nome):
        self.nome = nome
    def notificar_cliente(self):
        print(f'[ATENÇÃO] Pedido {self.nome} enviado!')
    def gerar_nota_fiscal(self):
        print(f'[Sistema] Nota Fiscal emitida para {self.nome}!')
    
estados = ['novo', 'em preparo', 'enviado', 'cancelado']
transicoes = [
    {
        'trigger': 'processar',
        'source': 'novo',
        'dest' : 'em preparo'
    },
    {
        'trigger': 'enviar',
        'source': 'em preparo',
        'dest' : 'enviado',
        'after' : ['notificar_cliente', 'gerar_nota_fiscal']
    },
    {
        'trigger': 'cancelar',
        'source': ['novo', 'em preparo'],
        'dest' : 'cancelado'
    }
]
p = Pedido('12345')
# print(semaforo.__dict__)
maquina = Machine(
    model = p,
    states = estados,
    transitions = transicoes,
    initial = 'novo'
)

# print(maquina)

print(p.state)
p.processar()
print(p.state)
p.cancelar()
print(p.state)
# print(p.state)
# p.enviar()
# print(p.state)

