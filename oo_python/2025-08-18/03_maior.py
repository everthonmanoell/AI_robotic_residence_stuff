def le_numeros_arquivo(nome):
    with open(nome) as arq:
        resultado = []
        for linha in arq:
            resultado.append(int(linha))
        return resultado

numeros = le_numeros_arquivo('03-numeros.txt')
print(numeros)
print(max(numeros))
print(sorted(numeros))

# with open('03-numeros.txt') as arq: 
#     maior_numero = 0
#     soma_numeros = 0
#     contador = 0
#     for linha in arq: 
#         valor_atual = int(linha)
#         contador += 1
#         soma_numeros += valor_atual
#         if valor_atual > maior_numero:
#             maior_numero = valor_atual
#     print(maior_numero)
#     print(soma_numeros/contador)