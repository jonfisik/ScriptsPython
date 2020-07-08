'''Exercício Python 055: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.'''
print('-=-=-=-=-=-'*4)
titulo = str('MAIOR E MENOR')
print('{:^44}'.format(titulo))
print('-=-=-=-=-=-'*4)
#---------------------------------------------------
menor = 0
maior = 0
for c in range(1,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(c)))
    if c == 1:
        peso = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('-----------'*4)
print('O maior peso lido foi de {} kg.'.format(maior))
print('O menor poeso lido foi de {} kg.'.format(menor))
print('-=-=-=-=-=-'*4)
