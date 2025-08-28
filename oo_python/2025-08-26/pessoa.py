#Dataclasses
from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int 

class PessoaTradicional:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

if __name__ == '__main__':
    p = PessoaTradicional('Leopoldo', 40)
    print(p.nome)
    print(p.idade)
    print(p, id(p))
    outra_pessoa = Pessoa(nome='Leo', idade=40)
    print(outra_pessoa, id(outra_pessoa))
    print( p == outra_pessoa )