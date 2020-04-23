'''Faça um programa que calcule o preço de um produto com 5% de desconto. 23/04/2020'''
print('=+='*18)
valor = float(input('Qual o valor do produto em reais: '))
desconto = valor * 0.05
print('%5 de {:.2f} é {:.2f}.'.format(valor, desconto))
print('O valor a ser pago será {:.2f}. Parabéns pelas compra.'. format(valor - desconto))
print('=+='*18)