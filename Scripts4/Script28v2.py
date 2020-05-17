'''Jonatan Paschoal  - 15 /05 /2020. Condicionais if, else. Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O computador deverá escrever na tela se o usuário venceu ou perdeu.'''
from random import randint
from time import sleep
print('-=-'*15)
nome = str(input('Olá, qual seu nome? ')).strip()
print('\n')
print('{}, eu sou o computador.'.format(nome))
print('Eu pensei em um número...')
print('Entre 0 e 5.')
x = randint(0,5)
print('\n')
print('Tente advinhar que número pensei. hahahaha...')
print('-=-'*15)
num = int(input('Que número pensei? '))
print('SUSPENSE...')
print('Não tenha medo {} hahaha.'.format(nome))
#--------------------------------------------
sleep(3)
if num == x:
    print('Parabéns você VENCEU!!!')
else:
    print('Você perdeu hahahaha...')
    print('Pensei no múmero {}.'.format(x))
    print('Mais sorte da próxima vez.')
print('Não demore para voltar!')
print('-=-'*15)
