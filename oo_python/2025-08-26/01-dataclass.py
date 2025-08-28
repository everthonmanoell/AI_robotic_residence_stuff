from dataclasses import asdict, astuple, dataclass, field, replace
from typing import List


@dataclass
class Equipe:
    nome : str
    membros : List[str] = field(default_factory = list)

class EquipeTradicional: 
    def __init__(self, nome, membros = []):
        pass

@dataclass(frozen=True)
class Ponto:
    x: int
    y: int 

@dataclass(kw_only=True)
class Conexao:
    host: str = 'localhost'
    porta: int = 5423
    ssl : bool = field(default=False)

@dataclass
class Usuario:
    nome_usuario : str
    email : str
    def __post_init__(self):
        if '@' not in self.email:
            raise ValueError('Email inválido!')

@dataclass
class LoginCIn:
    nome_completo : str
    nome_usuario : str = field(init=False)
    email : str = field(init=False)

    def __post_init__(self):
        nomes = self.nome_completo.lower().split(' ')
        iniciais = [nome[0] for nome in nomes]
        self.nome_usuario = ''.join(iniciais)
        self.email = self.nome_usuario+'@cin.ufpe.br'

@dataclass(frozen=True)
class Teste:
    x : int
    L : list


if __name__ == '__main__':
    t = Teste(13, [1,2,3,4])
    print(t, id(t), id(t.L))
    # t.x = 15
    t.L.append(15)
    print(t, id(t), id(t.L))
    # t = Teste(15, [1])
    # print(t)
    # t = Teste(14, [])
    # print(t)
    # l = LoginCIn('Leopoldo Motta Teixeira') 
    # print(l.nome_completo)  
    # print(l) 
    # print(asdict(l))
    # print(astuple(l))
    # # l.nome_usuario = 'leopoldo'
    # print(replace(l, nome_completo='Leopoldo Teixeira'))
    # print(l)
    # u = Usuario('leopoldomt', 'email_invalido@')   
    # print(u) 
    # c = Conexao('host', 8888)
    # c = Conexao(host='host', porta=8888)
    # print(c)
    # e1 = Equipe(1)
    # e2 = Equipe('Outro nome', ['1','2','3'])
    # print(e1)
    # print(e2)
    # p = Ponto(12,25)
    # print(p)
    # print(p.x, p.y)
    # # p.x = 15
    # p.y = 18
    # print(p)
    # print(p.x, p.y)