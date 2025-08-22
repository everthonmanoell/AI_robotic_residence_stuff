import sys

if len(sys.argv) != 3:
    print(f'Uso indevido, tem que chamar python3 {sys.argv[0]} <a> <b>')
    sys.exit(2)

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(a+b)
    sys.exit(0)
except ValueError:
    print('Erro! Os argumentos devem ser numéricos!')
    sys.exit(2)