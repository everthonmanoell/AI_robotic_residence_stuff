def menor(a, b):
    if a < b:
        return a
    if b < a:
        return b
    
    return a or b
    
n1 = int(input("Digite um valor inteiro qualquer: "))
n2 = int(input("Digite um valor inteiro qualquer: "))

print(menor(n1, n2))