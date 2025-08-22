import sys

print('Nome do script sendo executado:', sys.argv[0])
if len(sys.argv) > 1:
    print('Argumentos adicionais:', sys.argv[1:])
