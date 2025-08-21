import time

# t = time.localtime()
# print("Ano:", t.tm_year, "Mês:", t.tm_mon, "Dia:", t.tm_mday)

# inicio = time.time()
# soma = 0
# for i in range(100000000):
#     soma = soma + i
# fim = time.time()
# print("Tempo decorrido:", fim-inicio, "segundos")

print('Vou fazer algo já já, só descansar uns segundinhos aqui...')
time.sleep(5)
print('Pronto, agora vamos!')

inicio = time.perf_counter()
soma = 0
for i in range(100000000):
    soma = soma + i
fim = time.perf_counter()
print("Tempo decorrido:", fim-inicio, "segundos")