'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
print('---------------'*3)
ano = int(input('Digite um ano qualquer: '))
print('---------------'*3)
if ano % 4 == 0 or ano % 400 == 0:
    print('O ano {} é bissexto!'.format(ano))
else:
    print('O ano {} não é bissexto!'.format(ano))
print('---------------'*3)