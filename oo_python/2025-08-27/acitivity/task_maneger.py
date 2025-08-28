import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto


class Prioridade(Enum):
    BAIXA = auto()
    MEDIA = auto()
    ALTA = auto()
    
    def __str__(self):
        return self.name
    
    @property
    def peso(self):
        return self.value


class NaoVazio:
    def __set_name__(self, owner, name):
        self.name = name 

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"O atributo '{self.name}' deve ser uma string.")
        if len(value.strip()) == 0:
            raise ValueError(f"O atributo '{self.name}' não pode ser vazio ou conter apenas espaços.")
        instance.__dict__[self.name] = value

class DataNaoPassada():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, datetime):
            return TypeError(f'O atributro {type(value)} não é do tipo datetime. Informe uma data válida do tipo datetime.')
        if value < datetime.now():
            raise ValueError(f"O atributo '{self.name}' não pode ser uma data passada.")
        instance.__dict__[self.name] = value

@dataclass
def Tarefa():
    nome: str
    prazo: datetime
    prioridade: Prioridade
    concluida: bool

    nome = NaoVazio()
    prazo = DataNaoPassada()
    def __init__(self, nome: str, prazo: datetime, prioridade: Prioridade = Prioridade.MEDIA, concluida: bool = False):
        self.nome = nome
        self.prazo = prazo
        self.prioridade = prioridade
        self.concluida = concluida
    
    @property
    def nome(self):
        return self.nome
    
    @property
    def prazo(self):
        return self.prazo
    
    @property
    def prioridade(self):
        return self.prioridade
    
    @property
    def concluida(self):
        return self.concluida

    def __str__(self):
        status = "Concluída: ✓ " if self.concluida else "Pendente"
        return f'[{self.prioridade}] {self.prazo} - {self.nome}  ({status})'


def GerenciadorTarefas():
    lista_tarefas = field(default_factory=list)

    def __init__(self):
        self.lista_tarefas = []

    def adicionar_tarefa(self, tarefa: Tarefa):
        if isinstance(tarefa, Tarefa):
            self.lista_tarefas.append(tarefa)
        else:
            return f"Erro: O objeto {tarefa} não é do tipo Tarefa."
        
    def listar_tarefas(self, incluir_concluidas = True, enumerar = True, ordem_por='propriedade'):
        tarefas = self.lista_tarefas


        # filtrar concluídas se necessário
        if not incluir_concluidas:
            tarefas = [t for t in tarefas if not t.concluida ]


        # ordenar 
        if ordem_por.lower() == "prioridade":
            tarefas = sorted(tarefas, key=lambda t: t.prioridade.peso, reverse=True)
        elif ordem_por.lower() == "prazo":
            tarefas = sorted(tarefas, key=lambda t: t.prazo)

        ## Persistência
        def salvar_json(self, caminho):
            tarefas_json = [
                {
                    'nome': t.nome,
                    'prazo': t.prazo.strftime('%Y-%m-%d'),
                    'prioridade': str(t.prioridade),
                    'concluida': t.concluida  
                }
                for t in self.lista_tarefas
            ]

            with open(caminho, 'w') as f:
                json.dump(tarefas_json, f, indent=4)

                    
            

        # def carregar_json(self, caminho):
        #     with open(caminho, 'r') as f:
        #         tarefas_json = json.load(f)
            
        #     self.lista_tarefas = [
        #         Tarefa(
        #             nome=t['nome'],
        #             prazo=datetime.strptime(t['prazo'], '%Y-%m-%d'),
        #             prioridade=Prioridade[t['prioridade']],
        #             concluida=t['concluida']
        #         )
        #         for t in tarefas_json
        #     ]

            

        def salvar_csv(self, caminho):
            pass

        def carregar_csv(self, caminho):
            pass