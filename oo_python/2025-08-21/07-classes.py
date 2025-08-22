#Aqui estamos definindo uma classe
class NomeDaClasse:
    pass
#Aqui estamos criando um objeto de uma classe em particular
x = NomeDaClasse()# x = new NomeDaClasse()
NomeDaClasse.__init__(x) # chamando o método init padrão herdado do object
# x.teste = 'leopoldo'
# print(x, type(x))
# print(x.teste)

# def m(x):
#     y = x
#     return x + 2
# print(m(2))
# # print(y)

# class Teste:
#     def __init__(self,x):
#         y = x #variável local dentro do __init__
#         self.x = x+2 #variável acessível fora do __init__
# t = Teste(2) #__init__(t,2)
# print(t.x)
# t.y = 5 #cria um novo atributo <y> dentro do objeto com o valor de 5
# print(t.y)

class ContaBanco:
    def __init__(self, cliente, saldo=0, juros=0.1): #construtor da classe
        self.cliente = cliente
        self.saldo = saldo
        self.juros = juros
    def adicionar_rendimento(self):
        self.saldo = self.saldo + (self.saldo*self.juros)
    def debitar(self, valor):
        if valor<=self.saldo:
            self.saldo = self.saldo - valor
            return True
        return False
    def creditar(self,valor):
        self.saldo = self.saldo + valor

# ContaBanco.__init__(c, 'Leopoldo', 50) # c aqui não está definito, ele não existe.

# c = ContaBanco('Leopoldo',50)
# print(c.cliente, c.saldo)
# c.adicionar_rendimento()
# print(c.cliente, c.saldo)

conta_luyara = ContaBanco('Luyara', 600)
# print(conta_luyara, type(conta_luyara))
# print(conta_luyara.cliente, conta_luyara.saldo)
# # conta_luyara.saldo = conta_luyara.saldo - 100
# if conta_luyara.debitar(100):
#     print('débito funcionou')
# print(conta_luyara.cliente, conta_luyara.saldo)
# if conta_luyara.debitar(2000):
#     print('débito funcionou 2k')
# conta_luyara.saldo = conta_luyara.saldo - 2000
# print(conta_luyara.cliente, conta_luyara.saldo)
# conta_luyara.adicionar_rendimento()
# conta_luyara.saldo = conta_luyara.saldo + (conta_luyara.saldo*0.01)
# print(conta_luyara.cliente, conta_luyara.saldo)

# conta_luyara.cliente = 'Luyaraaaa'
# conta_luyara.saldo = 600
# print(conta_luyara.cliente, conta_luyara.saldo)
# print('Se chegou até aqui, tudo ok!')
# conta_renan = ContaBanco('Renan')
# print(conta_renan.cliente)
# conta_renan.cliente = 'Renannnn'
# print(conta_renan.cliente, conta_renan.saldo)

L = [1,2,3]
print([L])
print([''.join(list("nome do autor"))])
class Livro:
    def __init__(self, t:str, a:list, e, num_pgs, edicao=1):
        self.titulo = t
        self.autores = list(a)
        self.editora = e
        self.qtde_paginas = num_pgs
        self.edicao = edicao