'''Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
print('-=-=-=-=-=-'*4)
titulo = str('MAIOR E MENOR')
print('{:^44}'.format(titulo))
print('-=-=-=-=-=-'*4)
for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
print('-=-=-=-=-=-'*4)