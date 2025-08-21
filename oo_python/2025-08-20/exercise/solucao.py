def find_max_calorias():
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

            max_elfo = max(elfos, key=elfos.get) # retorna a chave associada ao número máximo


            elfos_sorted = sorted(elfos.items(), key=lambda x: x[1] ,reverse=True)

            top3 = elfos_sorted[:3]

            return f'O elfo:{max_elfo} carrega a carga máxima de: {elfos[max_elfo]} e o top 3 são: {top3} (quantidade de elfo: {count})'


            
    except FileNotFoundError as e:
        print(e)
        return None
    
print( find_max_calorias())
    