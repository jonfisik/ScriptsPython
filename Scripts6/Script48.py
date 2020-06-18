'''Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('SOMA ÍMPARES DE 1 À 500')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
soma = 0
soma2 = 0
cont = 0
for c in range(1,501,2):
    soma = soma + (c+1)
    #print(c+1)
    if c % 3 == 0:
        cont = cont +1
        soma2 = soma2 + c
print('Soma de 1 à 500: {}.'.format(soma))
print(soma2)
print(cont)
print('=+=+=+=+=+=+=+=+='*3)