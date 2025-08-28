class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def __get__(self, instance, owner):
        print(type(self), type(instance), type(owner))
        return self
class Conta:
    banco = 'Nome do Banco'
    dono = Pessoa('Nome do Dono', 44)
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo


if __name__ == '__main__' :
    c = Conta('12345-X', 100)
    print(c, c.numero, c.saldo, c.banco)
    print(c.__dict__)
    print(Conta.__dict__)
    print(c.dono.nome)

    # p = Pessoa('Teste', 23)
    # print(p)
    # print(p.nome, p.idade)
    # print(p.__dict__)
    # print(p.nome, p.__dict__['nome'])