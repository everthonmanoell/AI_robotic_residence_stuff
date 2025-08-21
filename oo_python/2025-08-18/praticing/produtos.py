def obter_produtos(arquivo):
    produtos = {}

    with open(arquivo) as arq:
        for l in arq:
            line = l.split("|")

            id = line[0].strip()
            name = line[1].strip()
            value = float(line[2].strip())
            amount = int(line[3].strip())

            produtos[id] = {
                'name': name,
                'value': value,
                'amount': amount
            }
    return produtos

prod = obter_produtos('../05_produtos.txt')

for key, value in prod.items():
    print(f'{key}:{value}')