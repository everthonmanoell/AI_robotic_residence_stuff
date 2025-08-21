def obter_estoque(arquivo):
    produtos = {}
    with open(arquivo) as f:
        for linha in f:
            partes = linha.split("|")
            codigo = partes[0].strip()
            nome = partes[1].strip()
            valor = partes[2]#.strip()
            qtde = partes[3]#.strip()
            produtos[codigo] = {
                'nome' : nome,
                'valor' : float(valor),
                'qtde' : int(qtde)
            }
    return produtos
estoque = obter_estoque('05-produtos.csv')
for codigo, produto in estoque.items():
    print(codigo, produto)
print(estoque['PROD0014']['qtde'])