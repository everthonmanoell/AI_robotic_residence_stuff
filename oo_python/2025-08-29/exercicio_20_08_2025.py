"""
Dia 1: Contagem de Calorias


As renas do Papai Noel normalmente comem a ração comum de rena, mas precisam de muita
energia mágica para conseguir entregar presentes no Natal. Para isso, o lanche favorito
delas é um tipo especial de fruta estelar que só cresce no meio da selva. Os Elfos o convidaram
para participar da expedição anual até o pomar onde essas frutas crescem.
A selva é fechada demais para veículos ou acesso aéreo; por isso, a expedição dos Elfos
tradicionalmente segue a pé. Quando os barcos se aproximam da terra firme,
os Elfos começam a fazer o inventário de seus suprimentos.
Um item fundamental é a comida, em especial, o número de calorias que cada
Elfo está carregando (essa será a entrada do seu problema).
Os Elfos se revezam anotando a quantidade de calorias de cada refeição, lanche, ração,
um item por linha. Cada Elfo separa seu inventário do anterior
deixando uma linha em branco.
Por exemplo, suponha que eles anotem os seguintes valores:

1000
2000
3000


4000


5000
6000


7000
8000
9000


10000


Essa lista representa a comida carregada por cinco Elfos:
O primeiro Elfo leva 1000 + 2000 + 3000 = 6000 Calorias.
O segundo Elfo leva um item de 4000 Calorias.
O terceiro Elfo leva 5000 + 6000 = 11000 Calorias.
O quarto Elfo leva 7000 + 8000 + 9000 = 24000 Calorias.
O quinto Elfo leva um item de 10000 Calorias.


Como eles podem ficar com fome e precisar de lanches extras, é importante saber
qual Elfo está carregando mais calorias.
No exemplo acima, é o quarto Elfo, com 24000 Calorias.
Parte 1: Descubra qual Elfo está carregando mais calorias.
Quantas calorias esse Elfo carrega ao todo?
"""


# fazer uma lista de contagem de calorias, cada indice da lista é um elfo
# abrir o arquivo de calorias
# iniciar com um elfo e ir somando os números lidos nas linhas até achar '\n', ou seja, uma linha vazia
# quando achar o '\n', começar a contar para o próximo elfo da lista


contagem_calorias = []
with open("calorias.txt") as arquivo:
    soma_calorias = 0
    for linha in arquivo:
        if linha.strip() != "": # se a linha tiver um número
            soma_calorias += int(linha.strip()) # adiciona o valor
        else:
            contagem_calorias.append(soma_calorias)
            soma_calorias = 0
    # adiciona o último elfo na lista caso o arquivo não termine com linha em branco
    if soma_calorias > 0:
        contagem_calorias.append(soma_calorias)


# maior quantidade de calorias
quantidade_maxima_calorias = max(contagem_calorias)


# índice do elfo com essa quantidade
indice_elfo = contagem_calorias.index(quantidade_maxima_calorias)

print("----------------------------------------------------------")
print(f"O elfo {indice_elfo + 1} carrega o maior número de calorias: {quantidade_maxima_calorias}")

"""
Parte 2

Quando você termina esse cálculo, os Elfos percebem que o Elfo com mais calorias pode eventualmente ficar sem lanches.
Para evitar esse problema, eles decidem que gostariam de saber a soma das calorias carregadas pelos três Elfos que mais
carregam comida. Assim, mesmo que um deles fique sem suprimentos, ainda restam outros dois como reserva.

No exemplo anterior, os três maiores são:

Quarto Elfo → 24000 Calorias
Terceiro Elfo → 11000 Calorias
Quinto Elfo → 10000 Calorias
O total é 45000 Calorias. Parte 2: Descubra os três Elfos com mais calorias. Quantas calorias eles carregam no total?
"""
# ordenar a contagem de calorias
contagem_calorias_ordenada = sorted(contagem_calorias)

# segundo lugar
elfo_2_calorias = contagem_calorias_ordenada[-2] 
indice_elfo_2 = contagem_calorias.index(elfo_2_calorias)

# terceiro lugar
elfo_3_calorias = contagem_calorias_ordenada[-3] 
indice_elfo_3 = contagem_calorias.index(elfo_3_calorias)

print("----------------------------------------------------------")
print(f"Os elfos com mais calorias são:\n")
print(f"Elfo {indice_elfo + 1}: {quantidade_maxima_calorias}")
print(f"Elfo {indice_elfo_2 + 1}: {elfo_2_calorias}")
print(f"Elfo {indice_elfo_3 + 1}: {elfo_3_calorias}")
print("----------------------------------------------------------")
print(f"Total de calorias que eles carregam: {quantidade_maxima_calorias + elfo_2_calorias + elfo_3_calorias}")
print("----------------------------------------------------------")



