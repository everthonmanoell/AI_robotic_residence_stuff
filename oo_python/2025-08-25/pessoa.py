import datetime


class Pessoa(object):
    def __init__(self, nome, email, data_nascimento=None):#formato esperado '22/12/2012'
        self.nome = nome
        self.email = email
        self._minisegredo = ',,,'
        self.__segredo = '...'
        if data_nascimento != None:
            dia, mes, ano = data_nascimento.split('/')
            self.__data_nascimento = datetime.date(int(ano), int(mes), int(dia))
        else:
            self.__data_nascimento = None
    def primeiro_nome(self):
        return self.nome.split(' ')[0]
    def get_data_nascimento(self):
        return self.__data_nascimento
    # def set_data_nascimento(self, dia, mes, ano):
    #     self.__data_nascimento = datetime.date(int(ano), int(mes), int(dia))
    def set_data_nascimento(self, dia, mes, ano):
        if isinstance(dia,int) and isinstance(mes,int) and isinstance(ano,int):
            self.__data_nascimento = datetime.date(ano, mes, dia)
        else:
            raise ValueError('Precisa informar dia, mês e ano em formato numérico')
    def __outro_segredo(self):
        print('.......')
    def idade_em_dias(self):
        if self.__data_nascimento == None:
            raise ValueError('Data de nascimento não definida')
        else:
            delta = datetime.date.today() - self.__data_nascimento
            return delta.days
    def __str__(self):
        return f'{self.nome} ({self.email}) [{self.__segredo}]'

class Estudante(Pessoa):
    def __init__(self, nome, email, data_nascimento, creditos):
        # self.nome = nome
        # self.email = email
        super().__init__(nome,email, data_nascimento)
        self.creditos = creditos
    def incrementar_creditos(self, num_creditos):
        self.creditos = self.creditos + num_creditos
    def __str__(self):
        return f'{super().__str__()} - Cursou {self.creditos} créditos.'

class Professor(Pessoa):
    def __init__(self, nome, email, sala, disciplinas = [], data_nascimento = None):
        super().__init__(nome,email,data_nascimento)
        self.sala = sala
        self.disciplinas = disciplinas
    def ministrar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
    def __str__(self):
        return f'Prof. {self.nome}, Sala {self.sala}'
    
if __name__ == '__main__':
    e1 = Estudante('e1 s1', 'email1', '11/10/2000', 10)
    p1 = Professor('p1 s1', 'email_p_1', 'A1', [], '20/04/1980')
    print(e1, e1.get_data_nascimento(), e1.idade_em_dias())
    e1.set_data_nascimento(13,10,2000)
    print(e1, e1.get_data_nascimento(), e1.idade_em_dias())
    # print(p1, p1.__data_nascimento, p1.idade_em_dias())
    # print(e1.nome, p1.nome)
    # print(e1.email, p1.email)
    # # print(e1.__segredo, p1.__segredo)
    # e1.__outro_segredo()
    pessoa = Pessoa('pessoa 1', 'email pessoa1', '10/10/2010')
    print(pessoa, type(pessoa), pessoa._minisegredo)
    # print(pessoa._Pessoa__segredo)
    print(Pessoa.mro())
    # print(pessoa.mro())
    # print(pessoa.__segredo)
    # pessoa.__outro_segredo()