import csv
import json
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto


#=============================================================
# Parte 1 - Enumeração de Prioridades
#=============================================================
class Prioridade(Enum):
    BAIXA = auto()
    MEDIA = auto()
    ALTA = auto()
    
    def __str__(self):
        return self.name
    
    @property
    def peso(self):
        return self.value


#=============================================================
# Parte 2 - Descritores de Validação
#=============================================================
class NaoVazio:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        value = getattr(instance, self.private_name)
        return value
    
    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError(f"O atributo '{self.name}' deve ser uma string.")
        if len(value.strip()) == 0:
            raise ValueError(f"O atributo '{self.name}' não pode ser vazio ou conter apenas espaços.")
        setattr(instance, self.private_name, value.strip())
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

#=============================================================
# Parte 3 - ClasseDataclass Tarefa
#=============================================================
@dataclass
class Tarefa():
    nome: str
    prazo: datetime
    prioridade: Prioridade
    concluida: bool

    nome = NaoVazio()
    prazo = DataNaoPassada()
    def __init__(self, nome, prazo: datetime, prioridade: Prioridade = Prioridade.MEDIA, concluida: bool = False):
        self.nome = nome
        self.prazo = prazo
        self.prioridade = prioridade
        self.concluida = concluida
    

    def __str__(self):
        status = "Concluída: ✓ " if self.concluida else "Pendente"
        return f'[{self.prioridade}] {self.prazo} - {self.nome}  ({status})'

#=============================================================
# Parte 4 - Gerenciador de Tarefas
#=============================================================
class GerenciadorTarefas():
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
        
        return tarefas

    ## Persistência
    def salvar_json(self, caminho='./tarefas.json'):
        tarefas_json = [
            {
                'nome': t.nome,
                'prazo': t.prazo.strftime('%Y-%m-%d'),
                'prioridade': t.prioridade.name,  # salvo o name
                'concluida': t.concluida
            }
            for t in self.lista_tarefas
        ]

        with open(caminho, 'w') as f:
            json.dump(tarefas_json, f, indent=4)
        return f'Tarefas salvas em {caminho} com sucesso.'


    def carregar_json(self, caminho='./tarefas.json'):
        with open(caminho, 'r') as f:
            tarefas_json = json.load(f)

        self.lista_tarefas = [
            Tarefa(
                nome=t['nome'],
                prazo=datetime.strptime(t['prazo'], '%Y-%m-%d'),
                prioridade=Prioridade[t['prioridade']], 
                concluida=t['concluida']
            )
            for t in tarefas_json
        ]
        return self.lista_tarefas


    def salvar_csv(self, caminho= './tarefas.csv'):
        with open(caminho, 'w') as f:
            f.write("nome,prazo,prioridade,concluida\n")
            for t in self.lista_tarefas:
                f.write(f'{t.nome},{t.prazo.strftime("%Y-%m-%d")},{t.prioridade.name},{t.concluida}\n')
        return f'Tarefas salvas em {caminho} com sucesso.'


    def carregar_csv(self, caminho= './tarefas.csv'):
        with open(caminho, 'r') as f:
            next(f)  # pula cabeçalho
            self.lista_tarefas = []
            for line in f:
                campos = line.strip().split(',')
                self.lista_tarefas.append(
                    Tarefa(
                        nome=campos[0],
                        prazo=datetime.strptime(campos[1], '%Y-%m-%d'),
                        prioridade=Prioridade[campos[2]],  # bate com .name
                        concluida=campos[3].lower() == 'true'
                    )
                )
        return self.lista_tarefas


#=============================================================
# Parte 5 - Utilitário de Parsing
#=============================================================
class ParserTarefas:

    def _parse_data_iso(s: str) -> datetime:
        try:
            # Tenta formato ISO (YYYY-MM-DD)
            return datetime.strptime(s, '%Y-%m-%d')
        except ValueError:
            try:
                # Tenta formato brasileiro (DD/MM/YYYY)
                return datetime.strptime(s, '%d/%m/%Y')
            except ValueError:
                raise ValueError(
                    f"Data inválida: {s!r}. Use YYYY-MM-DD ou DD/MM/YYYY."
                )

    def _parse_prioridade(s: str) -> Prioridade:
        s = s.strip().upper()
        try:
            return Prioridade[s]

        except:
            raise ValueError(f'Prioridade inválida. {s!r}. Use BAIXA | MEDIA | ALTA')
    
    def __parse_bool(s: str) -> bool:
        s_normalizada = s.lower().strip()

        if s in ('1', 'yes', 'y', 'true', 't', 'sim', 's'):
            return True
        elif s in ('0', 'no', 'n', 'false', 'f', 'não', 'nao'):
            return False
        else:
            raise ValueError(f'Valor booleano inválido: {s!r}. Use sim/nao, true/false, 1/0.')


#=============================================================
# Parte 6 - CLI Simples
#=============================================================

if __name__ == "__main__":
    from datetime import datetime, timedelta
    gerenciador = GerenciadorTarefas()

    while True:
        print('=== Gerenciador de Tarefas ===')
        print('1) Carregar CSV')
        print('2) Carregar JSON')
        print('3) Salvar CSV')
        print('4) Salvar JSON')
        print('5) Adicionar Tarefa')
        print('6) Listar por propriedade')
        print('7) Listar por prazo')
        print('8) Marcar como concluída')
        print('9) Reabrir tarefa')
        print('0) Sair')
        escolha = input('Escolha uma opção: ').strip()
        # escolha = '5'

        
        if escolha == '1':
            log = gerenciador.carregar_csv()
            if log != None:
                print(log)
        elif escolha == '2':
            log = gerenciador.carregar_json()
            if log != None:
                print(log)
        elif escolha == '3':
            log = gerenciador.salvar_csv()
            if log != None:
                print(log)
        elif escolha == '4':
            log = gerenciador.salvar_json()
            if log != None:
                print(log)
        elif escolha == '5':
            nome = input("Nome da tarefa: ").strip()
            prazo = input('Digite o prazo no formado YYYY-MM-DD | DD/MM/AAAA: ' )
            prioridade = input('Digite a priodade BAIXA | MEDIA | ALTA: ').strip().upper()
            
            try:
                tarefa = Tarefa(
                    nome=nome,
                    prazo=ParserTarefas._parse_data_iso(prazo),
                    prioridade=ParserTarefas._parse_prioridade(prioridade)
                )
                gerenciador.adicionar_tarefa(tarefa)
            except ValueError as e:
                raise ValueError(f"Erro ao criar tarefa. Verifique os dados informados. {e.__traceback__}")
            
            print(f'Tarefa {tarefa.nome!r} adicionada com sucesso.')
        elif escolha == '6':
            tarefas = gerenciador.listar_tarefas(ordem_por='propriedade')
            for i, t in enumerate(tarefas):
                print(f'{i}. {t}')
        elif escolha == '7':
            tarefas = gerenciador.listar_tarefas(ordem_por='prazo')
            for i, t in enumerate(tarefas):
                print(f'{i}. {t}')
        elif escolha == '8':
            idx = int(input('Índice da tarefa a marcar como concluída: ').strip())
            try:
                gerenciador.lista_tarefas[idx].concluida = True
                print(f'Tarefa {gerenciador.lista_tarefas[idx].nome!r} marcada como concluída.')
            except IndexError:
                print(f'Erro: Índice {idx} inválido.')
        elif escolha == '9':
            idx = int(input('Índice da tarefa a reabrir: ').strip())
            try:
                gerenciador.lista_tarefas[idx].concluida = False
                print(f'Tarefa {gerenciador.lista_tarefas[idx].nome!r} reaberta com sucesso.')
            except IndexError:
                print(f'Erro: Índice {idx} inválido.')
        elif escolha == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida. Tente novamente.')  





