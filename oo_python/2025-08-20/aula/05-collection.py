import collections as col

L = [2, 2, 2, 2, 50, 2, 50, 2, 50, 50, 50, 7, 7, 7, 7]
contador = {}
valores_L = set(L)
# print(valores_L)
for valor in valores_L:
    contador[valor] = L.count(valor)
print(contador)


contador = col.Counter(L)
print(contador)

fila = col.deque([1, 2, 3, 4, 5])
print(fila)
print(type(fila))
fila.append(6)
fila.appendleft(0)
print(fila)
fila.pop()
print(fila)
fila.popleft()
print(fila)
