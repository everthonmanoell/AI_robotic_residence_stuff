from dataclasses import dataclass
from enum import Enum, IntEnum, StrEnum, auto


class DiaDaSemana(Enum):#(IntEnum):
    SEG = auto() #1
    TER = auto() #2
    QUA = auto() #3
    QUI = auto() #4
    SEX = auto() #5
    SAB = auto() #6
    DOM = auto() #7

@dataclass
class DiaSemana:
    nome: str
    def __post_init__(self):
        if not self.nome in ['segunda', 'sexta', 'domingo']:
            raise ValueError(f'Dia da semana inválido: {self.nome}')

class Status(IntEnum):
    OK = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500

class Estado(StrEnum):
    PE = 'Pernambuco'
    PB = 'Paraíba'
    AL = 'Alagoas'
    CE = 'Ceará'
    RN = 'Rio Grande do Norte'

    def comeca_com(self,letra):
        return self.value.startswith(letra)

if __name__ == '__main__':
    # for dia in DiaDaSemana:
    #     print(dia, dia.name, dia.value, type(dia), id(dia))
    # print('---')
    # print(DiaDaSemana.SEG == 1, type(DiaDaSemana.SEG), type(1))
    # print(DiaDaSemana.QUA < DiaDaSemana.SEX)
    # segunda = DiaDaSemana(1)
    # terca = DiaDaSemana.TER # DiaDaSemana(2)
    # print(segunda, type(segunda), id(segunda))
    # print(terca, type(terca), id(terca))
    # segunda = DiaSemana('segunda')
    # sexta = DiaSemana('sexta')
    # nona = DiaSemana('nona')
    # print(segunda, sexta, nona)
    # print(Status.OK == 200)
    # print(Status.NOT_FOUND, type(Status.NOT_FOUND), int(Status.NOT_FOUND), type(int(Status.NOT_FOUND)))
    print(Estado.PE, type(Estado.PE), Estado.PE.comeca_com('P'))
    for estado in Estado:
        print(estado, type(estado), estado.comeca_com('P'))