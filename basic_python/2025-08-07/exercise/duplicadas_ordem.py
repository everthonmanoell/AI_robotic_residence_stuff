
## Remover duplicatas mantendo ordem

# Escreva `sem_duplicatas(lst)` que recebe uma lista e retorna 
# outra lista sem valores repetidos, preservando apenas a 
# primeira ocorrência de cada elemento.

# print(sem_duplicatas([3,1,2,3,2,4,1]))  # [3,1,2,4]

def sem_duplicatas(lst):
    tupla = set()
    lista = []
    
    for e in lst:
        if e not in tupla:
            tupla.add(e)
            lista.append(e)
    
    
    
    
    return lista

print(sem_duplicatas([3,1,2,3,2,4,1]))