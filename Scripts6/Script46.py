'''Exercício Python 046: Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.'''
from time import sleep
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('CONTAGEM REGRESSIVA')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
print('Começando...')

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('=+=+=+=+=+=+=+=+='*3)
titulo2 = str('BUM! BUM! POOW!!! ')
print('{:^51}'.format(titulo2))
print('=+=+=+=+=+=+=+=+='*3)