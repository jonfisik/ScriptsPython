'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''
from random import randint
n = (randint(1,20),randint(1,20),randint(1,20),randint(1,20),randint(1,20))
print('-'*50)
print(f'O números sorteado foram {n}.')
print('-'*50)
print(f'O maior valor sorteado foi {max(n)}.')
print(f'O menor valor sorteado foi {min(n)}.')
print('-'*50)