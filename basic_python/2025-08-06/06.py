numeros = [1, 2, 4, 5, 6, 7, 8, 10, 23]
numeros2 = [1, 2, 4, 5, 6, 7, 8, 10, 23]

def retornar_soma_positivos(numeros):
    soma = 0
    for i in numeros:
        if i > 0:
            soma += i
    return soma

print(retornar_soma_positivos(numeros))



def soma_listas(l1, l2):
    sum_list = []
    
    if len(l1) == len(l2):
        for e in range(len(l1)):
            sum_list.append(l1[e] + l2[e])
    
    
    
    
    return sum_list


