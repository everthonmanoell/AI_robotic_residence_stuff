class Autor:
    def __init__(self, nome, nacionalidade):
        self.nome, self.nacionalidade = nome, nacionalidade

class Livro:
    def __init__(self, titulo, *autores):
        self.titulo, self.autores = titulo, autores
    def autores_formatados(self):
        return ', '.join([autor.nome for autor in self.autores])
    def __str__(self):
        return f'{self.titulo}, por {self.autores_formatados()}'

class Biblioteca:
    def __init__(self):
        self.livros = []
    def adicionar(self, livro: Livro):
        self.livros.append(livro)
    def listar_titulos(self):
        return [l.titulo for l in self.livros]
    def buscar_por_autor(self, autor):
        return [l for l in self.livros if autor in [a.nome for a in l.autores]]

if __name__ == '__main__':
    a1 = Autor('J.R.R. Tolkien', 'Inglês')
    a2 = Autor('Machado de Assis', 'Brasileiro')
    a3 = Autor('Teste 1', 'Brasileiro')
    a4 = Autor('Teste 2', 'Brasileiro')
    a5 = Autor('Teste 3', 'Brasileiro')
    l1 = Livro('Senhor dos Anéis', a1)
    l2 = Livro('Dom Casmurro', a2)
    l3 = Livro('Teste', a3, a4, a5)
    print(l1)
    print(l2)
    print(l3)
    print([a for a in l3.autores])
    print([a.nome for a in l3.autores])
    print('Teste 1' in [a for a in l3.autores])
    print('Teste 1' in [a.nome for a in l3.autores])
    b = Biblioteca()
    b.adicionar(l1)
    b.adicionar(l2)
    b.adicionar(l3)
    b.adicionar(Livro('Refactoring', Autor('Martin Fowler', 'Americano')))
    print(b.listar_titulos())
    print(b.buscar_por_autor('Martin Fowler'))
    print([l.titulo for l in b.buscar_por_autor('Martin Fowler')])