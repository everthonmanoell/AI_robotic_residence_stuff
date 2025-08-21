while True:
    n = int(input("Digite um número:"))

    if n > 0:
        while n > 0:
            n -= 1
            print(n + 1)
    else:
        print("Digite um numero maior que zero.")
