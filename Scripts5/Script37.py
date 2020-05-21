'''Escreva um programa que receba um valor e transforme para uma base numérica escolhida pelo usuário. Binário, octal ou hexadecimal.'''
print('=+=+=+=+=+=+=+=+='*3)
num = int(input('Digite o número inteiro: '))
print('Base BINÁRIA digite [ 2 ]')
print('Base OCTAL digite [ 8 ]')
print('Base HEXADECIMAL digite [ 16 ]')
base = int(input('Para qual base você quer transformar? '))
print('-----------------'*3)
if base == 2:
    print('O valor {} em binário é {}.'.format(num,bin(num)[2:]))
elif base == 8:
    print('O valor {} em octal é {}.'.format(num,oct(num)[2:]))
elif base == 16:
    print('O valor {} em hexadecimal é {}.'.format(num,hex(num)[2:]))
else:
    print('Opção INVÁLIDA tente novamente.')
print('=+=+=+=+=+=+=+=+='*3)