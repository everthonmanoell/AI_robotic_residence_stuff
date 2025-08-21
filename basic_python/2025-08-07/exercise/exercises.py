## Contador de vogais

# Escreva `conta_vogais(text)` que recebe uma string e retorna 
# quantas vogais (`a, e, i, o, u`) aparecem nela (maiúsculas ou minúsculas). 
# Use `for` para percorrer os caracteres.

# print(conta_vogais("Aprender Python é divertido!"))  # 9

## Soma de dígitos

# Escreva `soma_digitos(s)` que recebe uma string `s` contendo 
# dígitos e outros caracteres, e retorna a soma de todos os 
# dígitos encontrados. Dica, use a função `str.isdigit()`.

# print(soma_digitos("a1b2c3"))  # 6
# print(soma_digitos("abc"))     # 0

## Palavra mais longa

# Escreva `palavra_mais_longa(sentence)` que recebe uma frase e 
# retorna a **palavra** mais longa. Palavras são separadas por 
# espaços. Se houver empate, retorne a primeira. 
# Dica: use `str.split()` para quebrar uma string.

# print(palavra_mais_longa("Eu gosto de programar em Python"))  # "programar"

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

## Remover dígitos de string

# Escreva `remover_digitos(s)` que recebe uma string `s` e retorna 
# outra sem nenhum caractere numérico. Use `for` e `str.isdigit()`.

# print(remover_digitos("a1b2c3"))  # "abc"


## Remover duplicatas mantendo ordem

# Escreva `sem_duplicatas(lst)` que recebe uma lista e retorna 
# outra lista sem valores repetidos, preservando apenas a 
# primeira ocorrência de cada elemento.

# print(sem_duplicatas([3,1,2,3,2,4,1]))  # [3,1,2,4]


## Filtrar números pares

# Escreva `filtrar_pares(L)` que recebe uma lista de inteiros e 
# retorna uma nova lista contendo apenas os números pares.

# print(filtrar_pares([1,2,3,4,5,6]))  # [2,4,6]

## Quadrado dos valores

# Escreva `quadrado_valores(L)` que recebe uma lista de números e 
# retorna uma nova lista com cada valor elevado ao quadrado.

# print(square_values([1,2,3,4]))  # [1,4,9,16]

## Contar ocorrências

# Escreva `contar_ocorrencias(lst)` que recebe uma lista de valores 
# e retorna um dicionário `{valor: quantidade}` com a contagem de cada item.

# print(contar_ocorrencias(['a','b','a','c','b','a']))
# {'a': 3, 'b': 2, 'c': 1}

## Dicionário “vezes dez”

# Escreva `vezes_dez(inicio, fim)` que cria e retorna um dicionário 
# cujas chaves vão de `inicio` a `fim` (inclusive) e cada valor é a 
# chave multiplicada por 10.

# print(vezes_dez(3, 6))  # {3:30, 4:40, 5:50, 6:60}

## Fatoriais em dicionário

# Escreva `fatoriais(n)` que retorna um dicionário `{i: i!}` para 
# `i` de 1 até `n`. Lembre que `i! = i * (i-1) * … * 1`.

# print(fatoriais(5))  # {1:1, 2:2, 3:6, 4:24, 5:120}

## Histograma de caracteres

# Escreva `histograma(s)` que recebe uma string e imprime, 
# por letra, quantas vezes ela aparece, usando estrelas (`*`):

# histograma("banana")
## b *
## a ***
## n **

## Tupla ordenada

# Escreva `cria_tupla(a, b, c)` que recebe três números e retorna
# uma tupla `(menor, maior, soma)`.

# print(cria_tupla(5,3,9))   # (3,9,17)

## Desempacotar múltiplos retornos

# Escreva `minmax(lst)` que retorna dois valores: o menor e o maior 
# item de `lst`, em uma tupla. Demonstre como atribuir cada um a 
# variáveis separadas.

# mn, mx = minmax([7,2,9,3])
# print(mn, mx)  # 2 9

## Inverter um dicionário

# Escreva `invert_dict(d)` que recebe um dicionário simples 
# (valores únicos) e **inverte** suas chaves e valores.

# d = {1:"um", 2:"dois", 3:"tres"}
# invert_dict(d)
# print(d)  # {"um":1,"dois":2,"tres":3}

## Agrupar por inicial

# Escreva `agrupar_inicial(palavras)` que recebe uma lista de strings 
# e devolve dicionário em que cada chave é a letra inicial e o valor 
# é a lista de todas as palavras que começam com ela.

# print(agrupar_inicial(["alfa","beta","bola","amora"]))
# # {"a":["alfa","amora"], "b":["beta","bola"]}

## Agenda de telefones

# Implemente `adicionar_contato(agenda, nome, numero)` e `obter_numeros(agenda, nome)` 
# onde `agenda` é um dicionário que mapeia `nome` em uma lista de `numeros`.
# * `adicionar_contato` deve adicionar `numero` à lista, criando lista nova se necessário.
# * `obter_numeros` retorna a lista (ou `[]` se não existir).

# agenda = {}
# adicionar_contato(agenda,"pedro","123")
# adicionar_contato(agenda,"pedro","456")
# print(obter_numeros(agenda,"pedro"))  # ["123","456"]
# print(obter_numeros(agenda,"maria"))   # []

## Média por categoria

# Escreva `media_por_categoria(items)` que recebe lista de dicionários 
# com chaves `"categoria"` (string) e `"valor"` (número). 
# Retorna dicionário com cada categoria mapeada à média dos seus valores.

# dados = [
#   {"categoria":"A","valor":10},
#   {"categoria":"B","valor":20},
#   {"categoria":"A","valor":30},
# ]
# print(media_por_categoria(data))
# # {"A":20.0,"B":20.0}

## Validador de senha

# Escreva `validar_senha(pw)` que retorna `True` se a senha `pw` tiver 
# pelo menos oito caracteres, contiver ao menos uma letra maiúscula, 
# uma minúscula e um dígito. Use `any(...)` e loops.

# print(validar_senha("Abc123"))      # False  (muito curta)
# print(validar_senha("Abcdefgh"))    # False  (não tem dígito)
# print(validar_senha("abcdefg1"))    # False  (não tem maiúscula)
# print(validar_senha("Abcdefg1"))    # True