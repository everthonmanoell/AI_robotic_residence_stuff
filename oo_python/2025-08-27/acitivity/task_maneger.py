from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto


class Prioridade(Enum):
    BAIXA = auto()
    MEDIA = auto()
    ALTA = auto()
    
    def __str__(self):
        return self.name
    
    def peso(self):
        pesos = {
            Prioridade.BAIXA: 1,
            Prioridade.MEDIA: 2,
            Prioridade.ALTA: 3
        }
        return pesos[self]



class NaoVazio:
    def __set_name__(self, owner, name):
        self.name = name 

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"O atributo '{self.name}' deve ser uma string.")
        if len(value.strip()) > 0:
            raise ValueError(f"O atributo '{self.name}' não pode ser vazio ou conter apenas espaços.")
        instance.__dict__[self.name] = value

class DataNaoPassada():
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value < datetime.now():
            raise ValueError(f"O atributo '{self.name}' não pode ser uma data passada.")
        instance.__dict__[self.name] = value

@dataclass
def Tarefa():
    nome: str
    prazo: datetime
    prioridade: Prioridade
    concluida: bool = False

    nome = NaoVazio()
    prazo = DataNaoPassada()
    def __init__(self, nome: str, prazo: datetime, prioridade: Prioridade = Prioridade.MEDIA, concluida: bool = False):
        self.nome = nome
        self.prazo = prazo
        self.prioridade = prioridade
        self.concluida = False
    

    def __str__(self):
        status = "Concluída: ✓ " if self.concluida else "Pendente"
        return (f"Tarefa: {self.nome}\n"
                f"Prazo: {self.prazo.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"Prioridade: {self.prioridade}\n"
                f"Status: {status}\n")


