palavra = input("Digite uma palavra: ")
letra_o = input("Digite a letra da ocorrencia: ")

i = 0
tam = len(palavra)

ocorrencias = 0

if tam > 0:

    if letra_o in palavra:
        while i < tam:
            i += 1 if palavra.find(letra_o) else 0
        print(f"A letra ({letra_o}) aparece: {i} vezes na palavra: {palavra}")
    else:
        print("Não existe essa letra na palavra.")
