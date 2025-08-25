class Biblioteca:
    def __init__(self, livro):
        self.livros = []
        self.livros.append(livro)

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def buscar_todos_livros(self):
        return self.livros

    def buscar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                return livro
        return None


class Autores:
    def __init__(self, nome):
        self.autores = []
        self.adicionar_autor(nome)

    def get_nome(self):
        return self.autores

    def adicionar_autor(self, autor):
        self.autores.append(autor)


class Livro:
    def __init__(self, titulo, ano, autores):
        self.titulo = titulo
        self.ano = ano
        self.autores = autores

    def get_livro(self):
        return (self.titulo, self.ano, self.autores.get_nome())


# Testes
autores = Autores("Doido")
print(autores.get_nome())

autores.adicionar_autor("Outro doido")
print(autores.get_nome())

livro1 = Livro("dunna", 2001, autores)
print(livro1.get_livro())

biblioteca1 = Biblioteca(livro1)
print(biblioteca1.buscar_livro("dunna").get_livro())
