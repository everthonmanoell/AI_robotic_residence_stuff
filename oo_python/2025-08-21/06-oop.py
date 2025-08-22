pessoa = {
    'nome' : 'Nome da pessoa',
    'data_nascimento' : '12/12/2012',
    'cpf' : '12345678900',
    'endereco' : 'endereco...'
    #...
}


class Pessoa:
    def __init__(self, nome, data_nasc, cpf, endereco, salario=0, bonus=0):
        self.nome = nome
        self.data_nascimento = data_nasc
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.bonus = bonus
    def valor_recebido(self):
        return self.salario + self.bonus
    def __str__(self): #método padrão chamado para usa print
        return f'{self.nome} ({self.cpf})'

print(pessoa, type(pessoa)) 
print('---')
p = Pessoa('Nome da pessoa', '12/12/2012', '12345678900', 'endereco...', 1500, 300)
o = Pessoa('Nome da pessoa', '12/12/2012', '98765432199', 'endereco...')
print(p, type(p))
print(o, type(o))

print(pessoa['cpf'], p.cpf, o.cpf)

print(f'O valor recebido por p é {p.valor_recebido()}')
print(f'O valor recebido por o é {o.valor_recebido()}')
print(p is o) # is compara hash dos objetos / compara se os objetos apontam para o mesmo endereço de memória. Nese caso, retorna False, pois foram criados em chamadas diferentes
print(type(Pessoa))
print(type(Pessoa.valor_recebido))
print(type(p))
print(type(p.valor_recebido))

x = str(p) # mesma coisa de chamar o __str__(self) do objeto p
print(p) # str(p)
print(p.__str__())


def m(): 
    return 'teste'
print(m,type(m))#type function
x = 1
print(x, type(x)) #type int
x = [1,2,3] 
print(x, type(x)) #type list
x = '2,3,1' #type str
print(x, type(x))

print("\n Estou aqui \n ")

def teste(*args): # (*)recebe um ou mais argumentos em forma de tupla
    print(args)
#teste()
print(type(teste()))
teste(1)
teste(1,2)
teste(1,'2',False)
print('---')

print("\n Estou aqui \n ")


def teste2(*args, x=0):
    print(x, args)
# teste2()
teste2(1)
teste2(1,2)
teste2(1,'2',False, [1,2,3], 3, x='teste')

print("\n Estou aqui \n ")

def teste3(**kwargs): #arugmento nomeado (dict)
    print(kwargs)
teste3()
teste3(x='arg x')
teste3(x='arg x', y=1, z=False, L = [1,2,3])