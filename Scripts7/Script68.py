'''Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo. '''
from random import randint
print('-=-'*15)
titulo = 'PAR OU ÍMPAR'
print('{:^45}'.format(titulo))
print('-=-'*15)
v = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou ímpar? [P/I] >>> ')).strip().upper()[0]
        print('---'*15)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
    print('Deu >> PAR <<' if total % 2 == 0 else 'Deu >> ÍMPAR <<')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!!!')
            v += 1
        else:
            print('Você PERDEU!!!')
            break
    elif tipo == 'I':
        if total % 2 == 0:
            print('Você PERDEU!!!')
            break
        else:
            print('Você VENCEU!!!')
            v += 1
    print('Vamos jogar novamente...')
print(f'GAME OVER! Você venceu {v} vez(es).')
print('---'*15)


