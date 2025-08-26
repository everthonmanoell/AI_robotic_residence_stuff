import datetime
from dataclasses import dataclass

"""o dataclass é um decorador em Python que simplifica a criação de classes que são principalmente usadas para armazenar dados. Ele automaticamente gera métodos especiais como __init__(), __repr__(), __eq__(), entre outros, com base nos atributos definidos na classe.
"""
@dataclass
class Livro(frozenset=True):
    titulo: str
    autor: str
    ano_publicacao: int
    isbn: str

    """o __post_init__ é um método especial em dataclasses que é chamado automaticamente após a inicialização do objeto.
    Ele é usado para realizar validações ou inicializações adicionais que não podem ser feitas diretamente na definição dos campos.
    """
    def __post_init__(self):
        if self.ano_publicacao <0:
            raise NotImplemented
        return 

    def idade_do_livro(self) -> int:
        ano_atual = datetime.datetime.now().year
        return ano_atual - self.ano_publicacao


if __name__ == "__main__":
    livro = Livro(titulo="1984", autor="George Orwell", ano_publicacao=1949, isbn="1234567890")
    print(f"Título: {livro.titulo}")
    print(f"Autor: {livro.autor}")
    print(f"Ano de Publicação: {livro.ano_publicacao}")
    print(f"ISBN: {livro.isbn}")
    print(f"Idade do Livro: {livro.idade_do_livro()} anos")