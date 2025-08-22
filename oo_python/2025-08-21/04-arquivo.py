import sys

if len(sys.argv) != 2:
    print(f'Uso indevido, tem que chamar python3 {sys.argv[0]} <nome_arquivo>')
    sys.exit(2)

try:
    with open(sys.argv[1]) as arq:
        conteudo = arq.read()
        print(conteudo)
        sys.exit(0)
except FileNotFoundError:
    print('Erro! O arquivo não existe!')
    sys.exit(2)
except:
    print('Algum outro erro!')
    sys.exit(1)