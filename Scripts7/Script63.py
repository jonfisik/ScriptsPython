'''Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. '''
print('-----------'*3)
titulo = 'SEQUÊNCIA DE FIBONACCI'
print('{:^30}'.format(titulo))
print('-----------'*3)
termos = int(input('Quantos termos você quer mostrar? '))
termo1 = 0
termo2 = 1
print('~'*30)
print('{} >> {}'.format(termo1,termo2), end='')
cont = 3
while cont <= termos:
    termo3 = termo1 + termo2
    print(' >> {}'.format(termo3), end='')
    termo1 = termo2
    termo2 = termo3
    cont += 1
print(' - FIM')
print('~'*30)