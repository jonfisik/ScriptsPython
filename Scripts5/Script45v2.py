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
#-------------------------------------------------
linha = ('-='*17)
print('{:^45}'.format(linha))
if jogador != 0 and jogador != 1 and jogador!= 2:
    erro = ('Opção inválida!!')
    print('{:^45}'.format(erro))
else:
    print('        O jogador jogou {}.'.format(item[jogador]))
    print('        O computador escolheu {}.'.format(item[computador]))
print('{:^45}'.format(linha))
#-------------------------------------------------
e = ('EMPATE !!!') 
c = ('COMPUTADOR VENCEU !!!')
j = ('JOGADOR VENCEU !!!')
#-------------------------------------------------
if computador == 0:#computador jogou pedra
    if jogador == 0:
        print('{:^45}'.format(e))
    elif jogador == 1:
        print('{:^45}'.format(j))
    elif jogador == 2:
        print('{:^45}'.format(c))
elif computador == 1:#computador jogou papel
    if jogador == 0:
        print('{:^45}'.format(c))
    elif jogador == 1:
        print('{:^45}'.format(e))
    elif jogador == 2:
        print('{:^45}'.format(j))
elif computador == 2:#computador jogou tesoura
    if jogador == 0:
        print('{:^45}'.format(j))
    elif jogador == 1:
        print('{:^45}'.format(c))
    elif jogador == 2:
        print('{:^45}'.format(e))
print('=+=+=+=+=+=+=+=+='*3)
