'''Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.'''
from random import randint
from time import sleep

print('-=-'*15)
titulo = 'MEGA SENA'
print(f'{titulo:^45}')
print('---'*15)

lista = list()
jogos = list()
quantidade = int(input('Quantos jogos você quer sortear? '))
total = 1
print('---'*15)
while total <= quantidade:
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('-='*5, f'SORTEANDO >> {quantidade} << JOGOS', '=-'*5)
for indice, linha in enumerate(jogos):
    print(f'Jogo {indice+1}: {linha}')
    sleep(0.5)

print('--'*8,' BOA SORTE ','--'*8 )
