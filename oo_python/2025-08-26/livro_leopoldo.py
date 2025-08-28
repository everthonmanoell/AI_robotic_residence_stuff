from dataclasses import dataclass

from pessoa import *


@dataclass
class Livro:
    titulo: str
    autor: Pessoa
    ano: int

    def __post_init__(self):
        if self.ano < 0:
            raise ValueError('O ano não pode ser negativo!')
        if not (isinstance(self.autor, Pessoa) or isinstance(self.autor, PessoaTradicional)):
            raise ValueError('O autor deve ser um objeto do tipo Pessoa!')
    def idade(self, ano_atual): 
        return ano_atual - self.ano
    
    def __lt__(self, outro_livro):
        if not isinstance(outro_livro, Livro):
            return NotImplemented
        return (self.autor, self.titulo, self.ano) < (outro_livro.autor, outro_livro.titulo, outro_livro.ano)
    
if __name__ == '__main__':
    livro1 = Livro('titulo', PessoaTradicional('nome', 43), 1974)
    livro2 = Livro('titulo', Pessoa('autor', 35), 1983)
    print(livro1, livro1.idade(2025))
    print(livro2, livro2.idade(2025))
    # print(livro1 < livro2)
    # print(livro1 < '12')
