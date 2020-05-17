'''Faça um programa que leia 3 números e diga qual é maior qual é menor.'''
print('---------------'*3)
print('Digite 3 números inteiros.')
a = int(input('a =  '))
b = int(input('b =  '))
c = int(input('c =  '))
print('---------------'*3)
maior = 0
menor = 0
if a > b and a > c:
    maior = a
    if a < b and a < c:
        menor = a
        if b > c:
            menor = c
        else:
            menor = b
print('{} {}'.format(maior, menor))
print('---------------'*3)