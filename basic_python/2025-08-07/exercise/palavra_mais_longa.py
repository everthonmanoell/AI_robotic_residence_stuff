## Palavra mais longa

# Escreva `palavra_mais_longa(sentence)` que recebe uma frase e 
# retorna a **palavra** mais longa. Palavras são separadas por 
# espaços. Se houver empate, retorne a primeira. 
# Dica: use `str.split()` para quebrar uma string.

# print(palavra_mais_longa("Eu gosto de programar em Python"))  # "programar"

def palavra_mais_longa(setence):
    longnest = ''
    
    palavras = setence.split()
    
    for p in palavras:
        if len(p) > len(longnest):
            longnest = p
    
    
    return longnest

print(palavra_mais_longa("Eu gosto de programar em Python"))