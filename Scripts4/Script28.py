'''Jonatan Paschoal  - 15 /05 /2020. Condicionais if, else. Escreva um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O computador deverá escrever na tela se o usuário venceu ou perdeu.'''
import random
print('---------------'*3)
print('O computador pensou em um número...')
print('Entre 0 e 5.')
x = random.choice([1,2,3,4,5])
print('Tente advinhar que número pensei. hahahaha...')
num = int(input('Advinhe o número que pensei: '))
if num == x:
    print('Parabéns você venceu!!!')
else:
    print('Você perdeu hahahah...')
    print('Pensei no múmero {}.'.format(x))
    print('Mais sorte da próxima vez.')
print('Não demore para voltar!')
print('---------------'*3)