'''Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.'''
from random import randint
from time import sleep
print('=+=+=+=+=+=+=+=+='*3)
item = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual sua jogada? '))
sleep(1)
print('( ( JO ) )')
sleep(1)
print('( ( KEN ) )')
sleep(1)
print('( ( PO ) )')
print('-='*15)
print('O jogador jogou {}.'.format(item[jogador]))
print('O computador escolheu {}.'.format(item[computador]))
print('-='*15)
if computador == 0:#computador jogou pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCEU!!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!!')
    else:
        print('Opção inválida!!')
elif computador == 1:#computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCEU!!!')
    else:
        print('Opção inválida!!')
elif computador == 2:#computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU!!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('Opção inválida!!')
print('=+=+=+=+=+=+=+=+='*3)
