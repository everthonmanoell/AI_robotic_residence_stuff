limite = int(input("Digite um número maior que 2: "))
i = 2


if limite >= 2:
    print("=")
    i = 1
    soma = 0
    while i <= limite:
        print(f"{i}+", end=" ")
        i += 1

    print(f" = {i}")
else:
    print("Digite um numero maior que 2")
