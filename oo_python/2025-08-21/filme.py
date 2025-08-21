class Filme:
    def __init__(self, titulo, genero, tempo_filme, diretor, ano=2025):
        self.titulo = titulo
        self.genero = genero
        self.tempo_filme = tempo_filme
        self.diretor = diretor
        self.ano = ano

    def set_titulo(self, titulo):
        self.titulo = titulo


f1 = Filme("Interestelar", "Ficcao", 2, 40, "2014")

print(f1.titulo)

f1.nota = 9.0
print(f1.nota)

f2 = Filme("Bruna Sufistinha", "Suspense", 1, "Kid", 69)

print(f"Titulo: {f2.titulo}")
print(f"Diretor: {f2.diretor}")
print(f"Ano de lançamento: {f2.ano}")
