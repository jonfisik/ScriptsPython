'''Exercício Python 052: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('PRIMOS')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
numero = int(input('Digite um número: '))
print('=+=+=+=+=+=+=+=+='*3)
tot = 0
print('\n')
for c in range(1,numero+1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end='')
print('\n')
print('\033[mO número {} foi divisível {} vezes!!!'. format(numero,tot)) #\033[m -> zera a cor
#----------------------------------------------------------------------
if tot == 2:
    print('O número é PRIMO!!!')
else:
    print('O número não é PRIMO!!!')
print('=+=+=+=+=+=+=+=+='*3)
