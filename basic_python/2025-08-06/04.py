def pede_numeros():
    array = []
    
    banner = 0
    
    while banner != '':
        numero = input('Digite um numero inteiro qualquer: ')
        array.append(int(numero))
        banner = str(numero)


    
    return array[:-1]

print(pede_numeros())