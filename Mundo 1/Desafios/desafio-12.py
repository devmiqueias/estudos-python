DESCONTO = 10
valorProduto = float(input('Digite o valor do produto: '))
valorDesconto = (DESCONTO / 100) * valorProduto
valorFinal = float(valorProduto - valorDesconto)

print('Você terá R$ {:.2f} de desconto, e o produto custará R$ {:.2f}.'.format(valorDesconto, valorFinal))

