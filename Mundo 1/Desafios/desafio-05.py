'''

Faça um progama que leia um número
Inteiro e mostra na tela o seu sucessor e
seu antecessor.

'''
numero = int(input('Digite um número: '))
s = numero + 1
a = numero - 1

print('Sucessor: {} - Antecessor: {}'.format(s, a))