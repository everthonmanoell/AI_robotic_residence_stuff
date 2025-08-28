from abc import ABC, abstractmethod
from dataclasses import dataclass, field, replace
from datetime import date
from enum import Enum, auto


class Departamento(Enum):
    RH = 121
    ENGENHARIA = 22
    QUALIDADE = 30
    VENDAS = 132
    def __str__(self):
        return f'*** {self.name} ({self.value}) ***'
@dataclass(order=True)
class Projeto:
    nome: str = field(compare=False) #ignore o nome quando for comparar/ordenar
    prazo: date

class NaoNegativo:
    def __set_name__(self, dono, nome):
        # salva um nome "privado" para o armazenamento real
        self._privado = "_" + nome

    def __get__(self, instancia, dono):
        if instancia is None:
            return self
        # se ainda não foi setado, levanta erro mais claro
        if self._privado not in instancia.__dict__:
            raise AttributeError(f"{self._privado[1:]} ainda não definido")
        return instancia.__dict__[self._privado]

    def __set__(self, instancia, valor):
        if not isinstance(valor, int):
            raise TypeError(f"{self._privado[1:]} deve ser int (centavos)")
        if valor < 0:
            raise ValueError(f"{self._privado[1:]} deve ser >= 0")
        instancia.__dict__[self._privado] = valor



class Funcionario(ABC):
    salario = NaoNegativo()
    def __init__(self, nome, salario, dept):
        self.nome = nome
        self.salario = salario
        self.departamento = dept
    @abstractmethod
    def trabalhar(self, *args, **kwargs):
        pass#toda subclasse deve implementar

class Gerente(Funcionario):
    def trabalhar(self, *args, **kwargs):
        return f'Gerente {self.nome} está gerenciando... Extras {args} {kwargs}'
class Desenvolvedor(Funcionario):
    def trabalhar(self, *args, **kwargs):
        stack = kwargs.get('stack', 'Python')
        return f'Desenvolvedor {self.nome} está programando em {stack}. Tarefas {args}'
class Empresa:
    def __init__(self):
        self.funcionarios = []
        self.projetos = []
        self.atribuicoes = {}
    def adicionar_funcionario(self, f):
        self.funcionarios.append(f)
        # self.atribuicoes[f.nome] = []
        self.atribuicoes.setdefault(f.nome, [])
    def adicionar_projeto(self, p):
        self.projetos.append(p)
        self.projetos.sort() #usar a ordenação de projetos (por prazo)
    def atribuir_projeto(self, f, p):
        if p not in self.projetos:
            raise ValueError('Projeto inexistente!')
        if f not in self.funcionarios:
            raise ValueError('Funcionário inexistente!')
        self.atribuicoes[f.nome].append(p)
        print(f'Atribuído {p.nome} a {f.nome} (Deadline: {p.prazo})')

if __name__=='__main__':
    # rh = Departamento.RH
    # if rh.value > 100:
    #     print('é administrativo')
    # print(rh)
    # f = Funcionario('Nome do Funcionário', 2500, Departamento.RH)
    e = Empresa()
    g = Gerente('Erico', 1200, Departamento.VENDAS)
    d = Desenvolvedor('Leopoldo', 450, Departamento.ENGENHARIA)
    e.adicionar_funcionario(g)
    e.adicionar_funcionario(d)
    # print(g.trabalhar('resolvendo bronca da residência', home_office = False, outro = 'teste'))
    # print(d.trabalhar('exemplo da empresa', 'exercício', stack = 'Javascript', outro = 'teste'))
    p1 = Projeto('Projeto1', date(2025, 12, 31))
    p2 = Projeto('Projeto 2', date(2025, 10, 31))
    e.adicionar_projeto(p1)
    e.adicionar_projeto(p2)

    e.atribuir_projeto(g,p2)
    e.atribuir_projeto(d,p1)
    print(e.projetos)
