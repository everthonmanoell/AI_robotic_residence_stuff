class Empregado: 
    def __init__(self, nome, salario = 0):
        self.nome = nome
        self.salario = salario
    def receber_aumento(self, percentual):
        self.salario += self.salario * percentual
    def trabalhar(self):
        print(self.nome, 'fazendo algo')
    def __str__(self):
        return f'< Empregado: nome={self.nome}, salario=R${self.salario} >'

class Chef(Empregado):
    def __init__(self, nome):
        super().__init__(nome, 15000)
    def trabalhar(self):
        print(self.nome, 'fazendo comida')

class Garcom(Empregado):
    def __init__(self, nome, salario=5000):
        super().__init__(nome, salario)
    def trabalhar(self):
        print(self.nome, 'atende clientes')
    def __str__(self):
        return f'{self.nome}'

class PizzaioloRobo(Empregado):
    def __init__(self, nome):
        super().__init__(nome)
    def trabalhar(self):
        print(self.nome, 'fazendo pizza')

if __name__ == '__main__':
    # chef = Chef('Jacquin', 10000)
    chef = Chef('Jacquin')
    # Chef.__init__(chef, 'Jacquin', 10000)
    garcom = Garcom('Amigo', 1000)
    robo = PizzaioloRobo('Denso')
    for empregado in (chef,garcom,robo):
        empregado.receber_aumento(0.1)
        empregado.trabalhar()
        print(empregado, isinstance(empregado, Empregado), type(empregado))
        print('---')
    