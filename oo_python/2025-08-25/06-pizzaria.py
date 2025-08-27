from empregados import Garcom, PizzaioloRobo


class Cliente:
    def __init__(self, nome):
        self.nome = nome
    def fazer_pedido(self, garcom):
        print(self.nome, 'faz pedido para', garcom)
    def pagar(self, garcom):
        print(self.nome, 'paga a conta para', garcom)

class FornoPizza:
    def assar(self):
        print('Forno está assando...')

class Pizzaria:
    def __init__(self):
        self.garcom = Garcom('Amigo')
        self.pizzaiolo = PizzaioloRobo('Denso')
        self.forno = FornoPizza()
    
    def tirar_pedido(self, nome_cliente):
        cliente = Cliente(nome_cliente)
        cliente.fazer_pedido(self.garcom)
        self.pizzaiolo.trabalhar()
        self.forno.assar()
        cliente.pagar(self.garcom)

if __name__ == '__main__':
    pizzaria = Pizzaria()
    pizzaria.tirar_pedido('Cliente Teste')
    print('---')