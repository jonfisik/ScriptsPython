'''Crie um programa que leia um número inteiro e diga se o número é PAR ou ÍMPAR'''
print('---------------'*2)
print('Digite número inteiro...')
num = int(input('Diremos se é PAR ou ÍMPAR: '))
print('     --------------------     ')
if num % 2 == 0:
    print('Você digitou um número PAR!')
else:
    print('O número digitado é ÍMPAR!')
print('---------------'*2)