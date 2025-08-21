def obter_notas(arquivo):
    notas = {}
    with open(arquivo) as f:
        for linha in f:
            partes = linha.split(",")
            nome = partes[0]
            notas[nome] = []
            for nota in partes[1:]:
                notas[nome].append(float(nota))
                # notas[nome].append(nota)
    return notas

boletim_geral = obter_notas('alunos.txt')
# print(boletim_geral)
for estudante, notas in boletim_geral.items():
    print(estudante, notas)