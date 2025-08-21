def normaliza(s):
    palavra = s.lower().strip()
    resultado = ''
    for c in palavra:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            resultado = resultado + c
    return resultado

def palindromo(palavra):
    print(palavra)
    if len(palavra) > 1:
        return palavra[0] == palavra[-1] and palindromo(palavra[1:-1])
    else:
        return True

# print(palindromo(normaliza('XANAX')))
# print('----')
# print(palindromo(normaliza('XABCX')))
# print('----')
# print(palindromo(normaliza('Socorram-me, subi no onibus em Marrocos')))

def soma_numeros(n):
    soma = 0
    
    for i in range(1,n+1):
        
        soma += i
    return soma

# print(soma_numeros(5)) #1+2+3+4+5 = 15

def soma_recursiva(n): 
    if n == 1:
        return 1 #caso base
    else:
        return n + soma_recursiva(n-1)

def soma_recursiva_alt(n):
    resultado = 0
    print(f'Prestes a calcular soma recursiva de {n}')
    if n == 1:
        resultado = 1
    else:
        resultado = n + soma_recursiva_alt(n-1)
    print(f'Acabei de calcular soma recursiva de {n} = {resultado}')
    return resultado

print(soma_recursiva_alt(5)) #1+2+3+4+5 = 15

# def teste(s):
#     print(s)
#     teste(s)

# teste('Leopoldo')

# while True:
#     print('Leopoldo')

def soma_numeros_lista(L):
    if len(L) > 1:
        return L[0] + soma_numeros_lista(L[1:])
    elif len(L) == 1:
        return L[0]
    else:
        return 0
# print(soma_numeros_lista([11,22,33,44,645]))
# print(soma_numeros_lista([1,2,3,4,5]))
# print(soma_numeros_lista([1,2,3,4]))
# print(soma_numeros_lista([1,2,3]))
# print(soma_numeros_lista([1,2]))
# print(soma_numeros_lista([1]))
# print(soma_numeros_lista([]))




def buscar_elemento(L,e):
    for i in range(len(L)):
        print(f'Vamos ver se o elemento na posição {i} é igual a {e}? L[{i}] == {L[i]}')
        if e == L[i]:
            return i

L = [1, 7, 14, 75, 87, 20, 2008, 15, 13, 4, 71, 45, 42, 34, 51, 52, 78, 33, 41, 40, 62, 90, 86, 99]
M = sorted(L)
# print(M)
procura = 2008

# i = buscar_elemento(M, procura)
# if i == None:
#     print(f'Elemento {procura} não está na lista L')
# else:
#     print(f'Elemento {procura} está na posição {i} da lista L')

def busca_binaria(L, esq, dir, e):
    if dir >= esq:
        meio = (esq + dir) // 2
        print(f'Vamos ver se o elemento na posição {meio} é igual a {e}? L[{meio}] == {L[meio]}')
        if L[meio] == e: 
            return meio
        elif e < L[meio]:
            return busca_binaria(L, esq, meio - 1, e)
        else:
            return busca_binaria(L, meio+1, dir, e)
    else:
        return None

def busca_binaria_alt(L, e):
    print(f'---')
    print(f'L agora é {L}')
    if len(L) > 0:
        meio = len(L) // 2
        print(f'Vamos ver se o elemento na posição {meio} é igual a {e}? L[{meio}] == {L[meio]}')
        if L[meio] == e: 
            return meio
        elif e < L[meio]:
            return busca_binaria_alt(L[0:meio], e)
        else:
            return busca_binaria_alt(L[meio+1:], e)
    else:
        return None

procura = 2009
# i = busca_binaria(M, 0, len(L)-1, procura)
# M = [20009]
# i = busca_binaria_alt(M, procura)
# if i == None:
#     print(f'Elemento {procura} não está na lista L')
# else:
#     print(f'Elemento {procura} está na posição {i} da lista L')