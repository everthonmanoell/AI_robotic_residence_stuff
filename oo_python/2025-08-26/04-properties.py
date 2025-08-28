from datetime import date


class Pessoa:
    def __init__(self, nome_completo, data_nascimento):
        self.__nome_completo = nome_completo # não existe self.nome
        self.__data_nascimento = data_nascimento

    @property
    def nome(self):
        return self.__nome_completo
    
    @property
    def primeiro_nome(self):
        return self.__nome_completo.split(' ')[0]
    
    @nome.setter
    def nome(self, novo_nome):
        if isinstance(novo_nome,str) and len(novo_nome) > 1:
            self.__nome_completo = novo_nome
        else:
            raise ValueError('Nome inválido')

    @property
    def idade(self):
        hoje = date.today()
        diferenca_em_anos = hoje.year - self.__data_nascimento.year
        nao_comemorou_niver_este_ano = (hoje.month, hoje.day) < (self.__data_nascimento.month, self.__data_nascimento.day)
        return diferenca_em_anos - nao_comemorou_niver_este_ano
        
    def get_nome(self):
        return self.__nome
    def set_nome(self, novo_nome):
        self.__nome = novo_nome

if __name__ == '__main__':
    p = Pessoa('Leopoldo Teixeira', date(2002,1,26))
    print(p.nome, p.primeiro_nome, p.idade)
    p.nome = 'Zé'
    print(p.nome, p.primeiro_nome, p.idade)
    # print(p.get_nome())
    #print(p._Pessoa__nome) #print(p.__nome)