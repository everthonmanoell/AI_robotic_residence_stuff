entrada = input("Digite uma palavra para verificar se é um palindromo: ")

if entrada.lower() == entrada[::-1].lower():
    print(f'A palavra ({entrada}) é um palindromo. ')
else:
    print('Não é um palindromo.')