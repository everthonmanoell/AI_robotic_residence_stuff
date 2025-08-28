# class Teste:
#     pass

# t = Teste()
# print(t.__dict__)
# # t.x = 10
# # print(t.__dict__)
# setattr(t,'x', 10)
# print(t.__dict__)
# print(getattr(t,'x'))

atributos = {'nome' : 'Teste', 'idade' : 40}
def fazer_aniversario(self):
    self.idade += 1
    print('Parabéns!')
metodos = { 'fazer_aniversario' : fazer_aniversario }
Pessoa = type('Pessoa', (), {**atributos, **metodos})

print(type(fazer_aniversario))
print(type(Pessoa))

p = Pessoa()
print(p.nome, p.idade)
print(type(p))
p.fazer_aniversario()
print(p.nome, p.idade)
print(isinstance(p,object))