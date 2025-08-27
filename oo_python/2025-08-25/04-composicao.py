class Motor:
    def __init__(self, potencia):
        self.potencia = potencia
        self.ligado = False
    def ligar(self):
        self.ligado = True
        print(f'Motor de {self.potencia}CV ligado agora.')
    def desligar(self):
        self.ligado = False
        print(f'Motor desligado.')
class Carro:
    def __init__(self, marca, modelo, potencia_motor):
        self.marca = marca
        self.modelo = modelo
        self.__motor = Motor(potencia_motor)
    def ligar_carro(self):
        self.__motor.ligar()
    def desligar_carro(self):
        self.__motor.desligar()
    def dirigir(self):
        if self.__motor.ligado:
            print(f'{self.marca} {self.modelo} em movimento...')
        else:
            print(f'{self.marca} {self.modelo} está com o motor desligado...')

class Item:
    def __init__(self, nome, preco, qtde = 1):
        self.nome, self.preco, self.qtde = nome, preco, qtde
    def subtotal(self):
        return self.preco * self.qtde

class Pedido:
    def __init__(self):
        self.itens = []
    def adicionar(self, item):
        if isinstance(item, Item):
            self.itens.append(item) 
    def adicionar_itens(self, *itens):
        for item in itens:
            if isinstance(item, Item):
                self.itens.append(item) 
    def total(self):
        return sum(i.subtotal() for i in self.itens)

if __name__ == '__main__':
    # hrv = Carro('Honda', 'HRV', 150)
    # hrv.dirigir()
    # hrv.ligar_carro()
    # hrv.dirigir()
    # hrv.dirigir()
    # # print(hrv.__motor.ligado)
    # hrv.dirigir()
    # hrv.desligar_carro()        
    # hrv.dirigir()
    # # print(hrv.__motor.ligado)
    item1 = Item('nome item 1', 5, 2)
    item2 = Item('nome item 2', 10)
    item3 = Item('nome item 3', 20, 3)
    pedido = Pedido()
    # pedido.adicionar(item1)
    # pedido.adicionar(item2)
    # pedido.adicionar('item3')
    # pedido.adicionar(item3)
    pedido.adicionar_itens(item1, item2, 'item3', item3)
    print(f'Total do pedido: R${pedido.total()}')