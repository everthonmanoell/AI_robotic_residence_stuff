palavra = input("Digite alguma coisa: ")

print("verificando segundo e penultimo caractere são iguais ")

if len(palavra) > 2:
    if palavra[1] == palavra[-2]:
        print(f"Os caracteres  ({palavra[1] }) e ({palavra[-2]}) são iguais")
    else:
        print(f"Os caracteres  ({palavra[1] }) e ({palavra[-2]}) são diferentes")
