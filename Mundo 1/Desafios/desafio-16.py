from math import trunc

while True:
    n = float(input('Digite um número real: '))
    valorAbsoluto = trunc(n)
    print('O valor absoluto de {} é {}.'.format(n, valorAbsoluto))
    if n == 0:
        break