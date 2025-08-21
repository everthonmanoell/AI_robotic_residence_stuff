## Contador de vogais

# Escreva `conta_vogais(text)` que recebe uma string e retorna 
# quantas vogais (`a, e, i, o, u`) aparecem nela (maiúsculas ou minúsculas). 
# Use `for` para percorrer os caracteres.

# print(conta_vogais("Aprender Python é divertido!"))  # 9

def contador_vogais(texto):
    contador = 0
    
    texto_n = texto.lower()
    
    for i in range(len(texto_n)):
        if texto_n[i] == 'a' or texto_n[i] == 'e'  or texto_n[i] == 'i' or texto_n[i] == 'o' or texto_n[i] == 'u':
            contador += 1
        
        
    
    
    
    return contador


texto = "Aprender Python é divertido!"

print(contador_vogais(texto))