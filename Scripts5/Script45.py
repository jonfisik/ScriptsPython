'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''
from time import sleep
import random
print('=+=+=+=+=+=+=+=+='*3)
print('''Sua opcões:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Qual é a sua jogada: '))
x = random.choice([0,1,2])
print('=+=+=+=+=+=+=+=+='*3)
if x == 0:
    pc = str('PEDRA')
elif x == 1:
    pc = str('PAPEL')
elif x == 2:
    pc = str('TESOURA')
#------------------------------------------------

#------------------------------------------------
sleep(1)
print('( ( JO ) )')
sleep(1)
print('( ( KEN ) )')
sleep(1)
print('( ( PO ) )')
print('=+=+=+=+=+=+=+=+='*3)
print('O computador escolheu {}'.format(pc))

print('=+=+=+=+=+=+=+=+='*3)
#if jogada == x:

