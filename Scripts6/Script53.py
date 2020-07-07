'''Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.'''
print('=+=+=+=+=+=+=+=+='*3)
titulo = str('PALÍDROMOS')
print('{:^51}'.format(titulo))
print('=+=+=+=+=+=+=+=+='*3)
frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]
print('-----------------'*3)
print(junto,inverso)
if inverso == junto:
    print('Temos um PALÍNDROME!')
else:
    print('A frase digitada não é um PALÍNDROME.')
print('=+=+=+=+=+=+=+=+='*3)
