'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''
from time import sleep
import random
print('=+=+=+=+=+=+=+=+='*3)
print('''Sua opcões:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogada = int(input('Qual é a sua jogada: '))

if jogada == 0:
    jogador = str('PEDRA')
elif jogada == 1:
    jogador = str('PAPEL')
elif jogada == 2:
    jogador = str('TESOURA')
#-----------------------------------------------    
x = random.choice([0,1,2])
print('=+=+=+=+=+=+=+=+='*3)
if x == 0:
    pc = str('PEDRA')
elif x == 1:
    pc = str('PAPEL')
elif x == 2:
    pc = str('TESOURA')
#------------------------------------------------
if jogada == x:
    resultado = str('EMPATE')
elif jogada == 0 and x == 1:
    resultado = str('PC VENCEU!')
elif jogada == 0 and x == 2:
    resultado = str('Jogador VENCEU!')
elif jogada == 1 and x == 0:
    resultado = str('Jogador VENCEU')
elif jogada == 1 and x == 2:
    resultado = str('PC VENCEU')
elif jogada == 2 and x == 0:
    resultado = str('PC VENCEU')
elif jogada == 2 and x == 1:
    resultado = str('Jogador VENCEU')
#------------------------------------------------
sleep(1)
print('( ( JO ) )')
sleep(1)
print('( ( KEN ) )')
sleep(1)
print('( ( PO ) )')
print('=+=+=+=+=+=+=+=+='*3)
print('O computador escolheu {}'.format(pc))
print('O jogador escolheu {}'.format(jogador))
print('Resultado: {}.'.format(resultado))
print('=+=+=+=+=+=+=+=+='*3)