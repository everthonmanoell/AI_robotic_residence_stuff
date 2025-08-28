class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome.upper()
        self.idade = idade
class Empregado(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome,idade)
        self.salario = salario 

if __name__ == '__main__' :
    p = Pessoa('Teste', 23)
    e = Empregado('Empregado', 28, 4000)
    # print(p.nome, p.idade)
    # print(e.nome, e.idade, e.salario)
    print(p.__dict__, e.__dict__)
    
    