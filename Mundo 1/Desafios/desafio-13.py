salario = float(input('Digite seu salário: '))
porcentagem = int(input('Digite o valor em (%) para calcular o seu aumento: '))
valorAcrescentado = (porcentagem / 100) * salario
salarioFinal = (salario + valorAcrescentado)

print('O seu salário atual é: R$ {:.2f}. Com o aumento de {}%, passará a ser: R$ {:.2f}'.format(salario, porcentagem, salarioFinal))