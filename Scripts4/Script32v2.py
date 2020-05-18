'''Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
from datetime import date
print('=+=+=+=+=+=+=+='*3)
ano = int(input('Digite um ano qualquer. \nColoque 0 para analisar o ano atual: '))
print('=+=+=+=+=+=+=+='*3)
#----------------------------------
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    texto1 = 'O ano {} é bissexto!'.format(ano)
    print('{:^45}'.format(texto1))
else:
    texto2 = 'O ano {} não é bissexto!'.format(ano)
    print('{:^45}'.format(texto2))
print('=+=+=+=+=+=+=+='*3)