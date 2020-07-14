'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
import random
print('------------'*4)
titulo = 'ADVINHAÇÃO'
print('{:^44}'.format(titulo))
print('------------'*4)
computador = random.choice([0,1,2,3,4,5,6,7,8,9,10])
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que consegue adivinhar?''')
acertou = False
palpites = 0
print('------------'*4)
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tente mais uma vez.')
        elif jogador > computador:
            print('Menos... Tente mais uma vez.')
print('Acertou com {} tentativas. Parabéns!!!'.format(palpites))
print('------------'*4)