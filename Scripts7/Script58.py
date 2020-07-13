'''Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.'''
import random
print('x-x-x-x-x-x'*4)
titulo = 'ADVINHAÇÃO'
print('{:^44}'.format(titulo))
print('x-x-x-x-x-x'*4)
num = random.choice([0,1,2,3,4,5,6,7,8,9,10])
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que consegue adivinhar?''')
palpite = int(input('Qual seu palpite? '))
x = y = z = 0
print('----------'*4)
while palpite != num:
    if palpite > num:
        print('Menos... Tente mais uma vez.')
        palpite = int(input('Qual seu palpite? '))
        x = x + 1
    if palpite < num:
        print('Mais... Tente mais uma vez.')
        palpite = int(input('Qual seu palpite? '))
        y = y + 1
z = x + y + 1
print('----------'*4)
print('Acertou com {} tentativas. PARABÉNS!!!'.format(z))
#print(num, palpite,z,x,y)
print('x-x-x-x-x-x'*4)