larg = float(input('Largura da parede: '))
alt = float(input('Largura da parede: '))
área = larg * alt
tinta = área / 2
print('Sua parede tem a dimensão de ({}) x ({}) e a sua ára é de {}m²'.format(larg, alt, área))
print('Para pinta sua parede você precisa de: {}L de tinta.'.format(tinta))