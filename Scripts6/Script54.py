'''Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('GRUPO DA MAIOR IDADE')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
#----------------------------------------------------------------
totmaior = 0
totmenor = 0
anoAtual = date.today().year
for c in range(1,8):
    n = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    idade = anoAtual - n
    if idade >= 21:
        totmaior = totmaior + 1
    else:
        totmenor = totmenor + 1
print('-----------------'*3)
print('Ao todo tivemos {} pessoa(s) com maior idade.'.format(totmaior))
print('E também tivemos {} pessoa(s) com menor idade.'.format(totmenor))
print('=+=+=+=+=+=+=+=+='*3)


        