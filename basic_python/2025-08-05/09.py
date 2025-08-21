nome_completo = input("Digite nome completo: ")

i = 0

tam = len(nome_completo)

ocorrencias = 0

if tam > 0:
    while i <= tam:
        char_atual = nome_completo[i].lower()
        
        ocorrencias += 1 if char_atual == 'a' or char_atual == 'e' or char_atual == 'i' or char_atual == 'o' or char_atual == 'u' else 0

print(ocorrencias)
