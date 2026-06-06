c = float(input('Informe a temperatura em ºC: '))
f = (c * 9/5) + 32
msg = 'A temperatura de {:.1f}º corresponde a {:.1f}ºF'.format(c, f)
print(msg)