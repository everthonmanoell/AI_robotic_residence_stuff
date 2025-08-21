def find_max_calorias():
    try:
        with open("calorias.txt") as arq:
            elfos = {}
            count = 1
            elfos[count] = 0

            for linha in arq:
                linha = linha.strip()

                if linha:  # linha não está vazia
                    if linha.isdigit():  # só processa se for número
                        elfos[count] += int(linha)
                else:  # linha em branco → próximo elfo
                    count += 1
                    elfos[count] = 0

            max_elfo = max(elfos, key=elfos.get)
            return max_elfo, elfos[max_elfo]

    except FileNotFoundError as e:
        print(e)
        return None

print(find_max_calorias())