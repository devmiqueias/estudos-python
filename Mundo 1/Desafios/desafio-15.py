dias = int(input('Digite a quantidade de dias: '))
km = float (input('Digite o KM percorrido: '))
total = (dias * 60) + (km * 0.15)
print('Total a ser pago: R$ {:.2f}'.format(total))