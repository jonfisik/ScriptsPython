'''Escreva um programa que leia a altura e largura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta é suficiente para 2 metros quadrados.'''
print('=+='*16)5
Largura = float(input('Qual a medida da largura em metros da parede? '))
Altura = float(input('Qual a medida da altura em metros da parede? '))
Area = Largura * Altura
litro = Area / 2
print('A área da parede é {:.2f} metros quadrados.'.format(Area))
print('Quantidade de litros {:.2f}.'.format(litro))
print('=+='*16)