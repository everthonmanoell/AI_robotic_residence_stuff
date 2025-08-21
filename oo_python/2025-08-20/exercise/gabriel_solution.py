def pegar_arquivo(path: str):
    data = []
    with open(path,'r') as arq:
        data = arq.readlines()
    
    return data


PATH = 'calorias.txt'

data = pegar_arquivo(PATH)

elfos = []

inicio, fim = 0, 0

for itm in range(len(data)):
    elfo = f'elfo_{itm}'

    if data[itm] == '\n':
        carga = [int(kal.strip()) for kal in data[inicio:itm]]
        elfos.append(
            {
                elfo: carga,
                'Total_kal': sum(carga)
            }
        )
        inicio = itm + 1

    elif itm == len(data) - 1:
        carga = [int(kal.strip()) for kal in data[inicio:itm]]
        elfos.append(
            { 
                elfo: carga,
                'Total_kal': sum(carga) 
            }
        )

print(elfos)