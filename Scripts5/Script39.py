'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo de alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo'''
from datetime import date
print('=+=+=+=+=+=+=+=+='*3)
titulo = 'ALISTAMENTO MILITAR'
print('{:^51}'.format(titulo))
print('-----------------'*3)
ano = float(input('Digite o ano de seu nascimento: '))
anoAtual = date.today().year

x = ano - anoAtual

x = int(abs(x))
y = int(abs(x - 18))
z = int(abs(anoAtual - y))
w = int(abs(anoAtual + y))
if x == 18:
    print('Você já completou {} anos.'.format(x))
    print('Você precisa se apresentar ainda esse ano.')
elif x > 18:
    print('Apresente-se imediatamente!!!')
    print('Já passaram {} anos do seu alistamento.'.format(y))
    print('Seu alistamento foi em {}.'.format(z))
elif x < 18:
    print('Você precisa esperar {} anos para sua apresentação.'.format(y))
    print('Seu alistamento será em {}'.format(w))
print('=+=+=+=+=+=+=+=+='*3)
