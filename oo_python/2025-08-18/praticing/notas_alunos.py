def obter_notas(arquivo):
    with open(arquivo) as arq:
        notas = {}

        for l in arq:
            conteudo = l.split(',')
            nome = conteudo[0]
            notas[nome] = []
            
            for n in conteudo[1:]:
                notas[nome].append(float(n))
        
        return notas
    
boletim = obter_notas("../alunos.txt")
for estudante, nota in boletim.items():
    print(f'{estudante} {nota}')
