n1 = float(input("Numero 1: "))
n2 = float(input("Numero 2: "))

operacao = input(
    "Qual operação você quprint(f'A soma é: {n1 + n2}')er fazer? Digite por extenso."
)

if operacao == "somar":
    print(f"A soma é: {n1 + n2}")
if operacao == "subtrair":
    print(f"A subtração é é: {n1 - n2}")
if operacao == "multiplicar":
    print(f"A multiplicação é: {n1 * n2}")
if operacao == "dividir":
    if n2 != 0:
        print(f"A subtração é é: {n1 / n2}")
