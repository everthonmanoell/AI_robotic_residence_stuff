def passos_iniciais():
    arquivo = open('02-exemplo.txt')
    print(arquivo)
    print(type(arquivo))
    conteudo = arquivo.read()
    print(type(conteudo))
    print(conteudo)

arquivo = open('02-exemplo.txt')
for linha in arquivo:
    print(linha,end='')
print(arquivo.read())
arquivo.close()
print(arquivo.read())


# with open('02-exemplo.txt') as arq:
#     for linha in arq:
#         print(linha, end='')

# print(arq.read())