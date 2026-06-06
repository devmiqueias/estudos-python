operador = ['(+) ADIÇÃO', '(-) SUBTRAÇÃO', '(/) DIVISÃO', '(//) DIVISÃO INTEIRA', '(%) MÓDULO "RESTO DA DIVISÃO', '(**) POTENCIA']
print(', '.join(operador))

op = input('Digite a operação desejada: ')
n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o valor 2: '))

if op == '+':
    resultado = (n1 + n2)
    print('A soma é: {}'.format(resultado))
elif op == '-':
    resultado = (n1 - n2)
    print('A diferença é: {}'.format(resultado))
elif op == '/':
    resultado = (n1 / n2)
    print('A divisão é: {}'.format(resultado))
elif op == '//':
    resultado = (n1 // n2)
    print('A divisão inteira é: {}'.format(resultado))
elif op == '%':
    resultado = (n1 % n2)
    print('O resto da divisão é: {}'.format(resultado))
elif op == '**':
    resultado = (n1 ** n2)
    print('A potência é: {}'.format(resultado))