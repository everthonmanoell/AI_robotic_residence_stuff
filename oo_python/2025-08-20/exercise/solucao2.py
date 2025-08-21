def encontrar_elfos():
    try:
        with open('calorias.txt') as arq:
            elfos = {}
            count = 1
            elfos[count] = 0
            for linha in arq:
                linha = linha.strip()

                if linha.isdigit():
                    elfos[count] += int(linha)
                else:
                    count += 1
                    elfos[count] = 0

            sorted_elfos = sorted(elfos.items(), key=lambda x: x[1] , reverse=True) #retorna uma lista

            top3 = sorted_elfos[:3]

            return f'O elfo que mais carregou comida foi o elfo: {top3[0][0]} que carregou: {top3[0][1]} e o top3 de carga foram: {top3} '

    except FileNotFoundError as e:
        print(e)


print(encontrar_elfos())