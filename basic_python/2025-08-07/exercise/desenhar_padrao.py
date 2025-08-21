## Desenhar padrão

# Escreva `padrao(s, n)` que imprime `n` linhas. A linha *i* (contando de 0) 
# deve começar em `s[i % len(s):] + s[:i % len(s)]` — ou seja, rotacione `s` 
# a cada linha.

# padrao("abcd", 6)
# # 
# # abcd
# # bcda
# # cdab
# # dabc
# # abcd
# # bcda


def padrao(s, n):
    for i in range(n):
        print(f'{s[i % len(s):]}{s[: i % len(s)]} ')
        
        
padrao('abcd', 6)