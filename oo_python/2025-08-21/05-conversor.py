import sys

if len(sys.argv) != 3:
    print(f'Uso indevido! python3 {sys.argv[0]} ESCALA(c2f,f2c) VALOR')
    sys.exit(2)

try:
    escala = sys.argv[1].strip().lower()
    temperatura = float(sys.argv[2])
    if escala == 'c2f':
        origem = 'celsius'
        destino = 'fahrenheit'
        conversao = (temperatura * 9/5) + 32
    elif escala == 'f2c':
        origem = 'fahrenheit'
        destino = 'celsius'
        conversao = (temperatura - 32.00) * (5.00 / 9.00)
    else:
        raise ValueError('Conversão inválida! Deve usar c2f ou f2c...')
    print(f'{temperatura} graus {origem} == {conversao} graus {destino}')

except ValueError as e:
    print(e)