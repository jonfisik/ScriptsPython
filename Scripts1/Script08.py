'''Jonatan Paschoal 22/04/2020 Desafio 8 - Faça um programa que receba um valor em metros e transforme para centímetros e milímetros.'''
print('=='*30)
x = float(input('Digite um valor em metros: '))
cent = x / 100
mili = x / 1000
print('{:.5f} em centímetros é {:.5f} e em milímetros {:.5f}.'.format(x, cent, mili))
print('=='*30)