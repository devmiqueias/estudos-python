'''

Crie um progama que leia quanto
dinheiro uma pessoa tem na carteira
e mostre quantos dólares ela pode 
comprar.

'''

real = float(input('Digite o valor para conversão: '))
dolar = 0.20
realConvertido = (real * dolar)
print('R$ {} pode comprar US$ {:.2f}.'.format(real, realConvertido))