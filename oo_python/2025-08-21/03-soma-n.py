import sys

if len(sys.argv) == 1:
    print(f'Uso indevido, tem que chamar python3 {sys.argv[0]} <a> <b> <c> ...')
    sys.exit(2)

try:
    # numeros = list(map(int, sys.argv[1:]))
    numeros = [int(n) for n in sys.argv[1:]]
    print(sum(numeros))
    sys.exit(0)
except ValueError:
    print('Erro! Os argumentos devem ser numéricos!')
    sys.exit(2)