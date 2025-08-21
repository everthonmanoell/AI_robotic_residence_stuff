## Soma de dígitos

# Escreva `soma_digitos(s)` que recebe uma string `s` contendo 
# dígitos e outros caracteres, e retorna a soma de todos os 
# dígitos encontrados. Dica, use a função `str.isdigit()`.

# print(soma_digitos("a1b2c3"))  # 6
# print(soma_digitos("abc"))     # 0

def soma_digitos(s):
    soma = 0
    
    for i in range(len(s)):
        if s[i].isdigit():
            soma += 1
    
    return soma

print(soma_digitos("a1b2c3"))