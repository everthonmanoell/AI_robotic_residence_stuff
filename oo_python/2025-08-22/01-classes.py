class Pessoa(object):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
    def primeiro_nome(self):
        return self.nome.split(' ')[0]
    def __str__(self):
        return f'{self.nome} ({self.email})'

class Estudante(Pessoa):
    def __init__(self, nome, email, creditos):
        # self.nome = nome
        # self.email = email
        super().__init__(nome,email)
        self.creditos = creditos
    def incrementar_creditos(self, num_creditos):
        self.creditos = self.creditos + num_creditos
    def __str__(self):
        return f'{super().__str__()} - Cursou {self.creditos} créditos até agora'

class Professor(Pessoa):
    def __init__(self, nome, email, sala, disciplinas = []):
        self.nome = nome
        self.email = email
        self.sala = sala
        self.disciplinas = disciplinas
    def ministrar_disciplina(self, disciplina):
        self.disciplinas.append(disciplina)
    def __str__(self):
        return f'Prof. {self.nome}, Sala {self.sala}'

if __name__ == '__main__':
    est = Estudante('Nome Estudante', 'email@cin.ufpe.br', 12)
    print(est, type(est))
    print(est.primeiro_nome(), est.creditos)
    est.incrementar_creditos(2)
    print(est.primeiro_nome(), est.creditos)
    prof = Professor('Um NomeComposto Professor', 'prof@cin.ufpe.br', 'A012', ['Python'])
    print(prof, type(prof))
    print(prof.primeiro_nome(), prof.disciplinas)
    prof.ministrar_disciplina('Android')
    print(prof.primeiro_nome(), prof.disciplinas)
    x = 1#int(1)
    L = [Estudante('nome', 'email', 10)]
    s = ''
    # print(type(x), type(L), type(s))
    print(type(x), isinstance(x, Estudante), isinstance(x, object))
    print(type(L), isinstance(L, list), isinstance(L, object))
    print(type(s), isinstance(s, Estudante), isinstance(s, object))
    print(type(est), isinstance(est, Estudante), isinstance(est, Pessoa), isinstance(est, object))
    print(type(prof),isinstance(prof, Professor), isinstance(prof, Pessoa), isinstance(prof, object))
    # prof.append('Java')

    est1 = Estudante('nome1', 'email1', 1)
    est2 = Estudante('nome2', 'email2', 2)
    est3 = Estudante('nome3', 'email3', 3)
    est4 = Estudante('nome4', 'email4', 4)