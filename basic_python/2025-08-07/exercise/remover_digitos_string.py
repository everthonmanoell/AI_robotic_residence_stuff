## Remover dígitos de string

# Escreva `remover_digitos(s)` que recebe uma string `s` e retorna 
# outra sem nenhum caractere numérico. Use `for` e `str.isdigit()`.

# print(remover_digitos("a1b2c3"))  # "abc"

def remover_digitos(s):
    resultado = ''
    
    for d in range(len(s)):
        if not s[d].isdigit():
            resultado += s[d]
             
    
    
    return resultado

print(remover_digitos('a1b2c3'))