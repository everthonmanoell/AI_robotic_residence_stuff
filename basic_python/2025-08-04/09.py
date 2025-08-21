studant_quantity = int(input("Quantos estudantes tem na sala? "))
tam_group = int(input("Qual o tamanho do grupo? "))


if studant_quantity % 2 == 0:
    print(f"Total de grupos necessários: {studant_quantity / tam_group}")
