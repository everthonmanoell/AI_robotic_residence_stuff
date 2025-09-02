import time
from enum import Enum, auto

from transitions import Machine


class Bebida(Enum):
    ESPRESSO = 5#Bebida.ESPRESSO.value
    LATTE = 7
    CAPPUCCINO = 8
NOMES = {
    'espresso' : Bebida.ESPRESSO,
    'latte' : Bebida.LATTE,
    'cappuccino' : Bebida.CAPPUCCINO
}
PRECOS = {
    Bebida.ESPRESSO : 5,#PRECOS[Bebida.ESPRESSO] ou PRECOS[NOMES['espresso']]
    Bebida.LATTE : 7,
    Bebida.CAPPUCCINO : 8
}

class MaquinaCafe:
    def __init__(self, estoque = {'agua':10, 'cafe':10, 'leite':5}):
        self.credito = 0
        self.bebida_selecionada = None
        self.troco = 0
        self.estoque = estoque
    
    def inserir(self, valor = 1):
        self.credito += valor
        print(f' Crédito: R${self.credito}')
    def inserir_uma_moeda(self):
        self.inserir(1)
    
    def cancelar_pedido(self):
        print(f' Cancelado. Devolução de R${self.credito}')
        self.credito = 0
        self.bebida_selecionada = None
    
    def requisitos(self, b):
        if b == Bebida.ESPRESSO:
            return {'agua' : 1, 'cafe' : 1}
        elif b == Bebida.LATTE:
            return {'agua' : 1, 'cafe' : 1, 'leite' : 1}
        elif b == Bebida.CAPPUCCINO:
            return {'agua' : 1, 'cafe' : 1, 'leite' : 2}
        else:
            raise ValueError('Bebida Desconhecida!')

    def tem_credito(self):
        if self.bebida_selecionada is None:
            return False
        return self.credito >= PRECOS[self.bebida_selecionada]
    def tem_estoque(self):
        if self.bebida_selecionada is None:
            return False
        req = self.requisitos(self.bebida_selecionada) #{'agua' : 1, 'cafe' : 1}
        #{'agua' : 1, 'cafe' : 1}
        # for produto, qtde in req.items():
        #     if self.estoque[produto]<qtde:
        #         return False
        # return True
        return all( self.estoque.get(produto,0)>=qtde for produto, qtde in req.items() )
    def reservar_itens(self):
        req = self.requisitos(self.bebida_selecionada) #{'agua' : 1, 'cafe' : 1}
        for produto, qtde in req.items():
            self.estoque[produto] -= qtde
        print(' Itens reservados: ', req, '| Estoque:', self.estoque)#TODO checar print com f''
    def preparar(self):
        print(f' Preparando {self.bebida_selecionada.name}...')
        time.sleep(0.5)
    def entregar_produto(self):
        print(f' Entregando {self.bebida_selecionada.name}!')
    def calcular_troco(self):
        preco = PRECOS[self.bebida_selecionada]
        self.troco = self.credito - preco
        print(f' Troco calculado: R${self.troco}')
    def entregar_troco(self):
        if self.troco > 0:
            print(f' Entregando troco: R${self.troco}')
        self.config_inicial()
    def config_inicial(self):
        self.troco = 0
        self.credito = 0
        self.bebida_selecionada = None
    
    def pode_preparar(self):
        esta_ok = self.tem_credito() and self.tem_estoque()
        if not esta_ok:
            if self.bebida_selecionada is None:
                print(' Nenhuma bebida selecionada!')
            elif not self.tem_credito():
                print(f' Crédito insuficiente (R${self.credito}, mas precisa de R${PRECOS[self.bebida_selecionada]}).')
            elif not self.tem_estoque():
                print(f' Sem estoque para esta bebida.')
        return esta_ok
    
    def on_enter_PREPARANDO(self):
        self.reservar_itens()
        self.preparar()

    def on_enter_ENTREGANDO(self):
        self.entregar_produto()
    
    def on_enter_TROCO(self):
        self.entregar_troco()
    
    def on_enter_ERRO(self):
        print(' ERRO: Crédito insuficiente ou sem estoque. Cancelando compra e devolvendo crédito.')
        print(f' Devolução: R${self.credito}')
        self.credito = 0
        self.bebida_selecionada = None

class Estados(Enum):
    AGUARDANDO_MOEDA = auto()
    CREDITO = auto()
    PREPARANDO = auto()
    ENTREGANDO = auto()
    TROCO = auto()
    ERRO = auto()
    MANUTENCAO = auto()

transicoes = [
    {
        'trigger' : 'inserir_moeda',
        'source'  : Estados.AGUARDANDO_MOEDA,
        'dest'    : Estados.CREDITO,
        'after'   : 'inserir_uma_moeda'
    },
    {
        'trigger' : 'inserir_moeda',
        'source'  : Estados.CREDITO,
        'dest'    : Estados.CREDITO,
        'after'   : 'inserir_uma_moeda'
    },
    {
        'trigger' : 'selecionar',
        'source'  : Estados.CREDITO,
        'dest'    : Estados.PREPARANDO,
        'conditions' : 'pode_preparar'#Precisa ser verdade para funcionar
    },
    {
        'trigger' : 'selecionar',
        'source'  : Estados.CREDITO,
        'dest'    : Estados.ERRO,
        'unless'  : 'pode_preparar'
    },
    {
        'trigger' : 'preparo_ok',
        'source'  : Estados.PREPARANDO,
        'dest'    : Estados.ENTREGANDO
    },
    {
        'trigger' : 'entrega_ok',
        'source'  : Estados.ENTREGANDO,
        'dest'    : Estados.TROCO,
        'before'  : 'calcular_troco'
    },
    {
        'trigger' : 'troco_ok',
        'source'  : Estados.TROCO,
        'dest'    : Estados.AGUARDANDO_MOEDA
    },
    {
        'trigger' : 'manutencao',
        'source'  : [Estados.AGUARDANDO_MOEDA, Estados.CREDITO, Estados.ENTREGANDO, Estados.TROCO, Estados.ERRO],
        'dest'    : Estados.MANUTENCAO
    },
    {
        'trigger' : 'retornar',
        'source'  : Estados.MANUTENCAO,
        'dest'    : Estados.AGUARDANDO_MOEDA
    },
    {
        'trigger' : 'resetar',
        'source'  : Estados.ERRO,
        'dest'    : Estados.AGUARDANDO_MOEDA
    },
    {
        'trigger' : 'cancelar',
        'source'  : Estados.CREDITO,
        'dest'    : Estados.AGUARDANDO_MOEDA,
        'after'   : 'cancelar_pedido'
    }
]

m = MaquinaCafe()
maq_estados = Machine(
    model = m,
    states = Estados, 
    transitions = transicoes, 
    initial = Estados.AGUARDANDO_MOEDA
)
