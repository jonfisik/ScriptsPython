'''Faça um programa que leia 3 números e diga qual é maior qual é menor.'''
print('---------------'*3)
print('Digite 3 números inteiros.')
a = int(input('a =  '))
b = int(input('b =  '))
c = int(input('c =  '))
print('---------------'*3)
# testando menor
menor = a
if b < a and b < c:
    maior = b
if c < a and c < b:
        menor = c
# testando maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('Menor: {}. Maior: {}.'.format(menor, maior))
print('---------------'*3)